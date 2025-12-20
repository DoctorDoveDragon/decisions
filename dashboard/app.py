import streamlit as st
import pandas as pd
import numpy as np
import io
import altair as alt
from typing import List

st.set_page_config(page_title="Decisions Dashboard", page_icon="🧭", layout="centered")

# --- Helpers and session state initialization ---

def init_state():
    if "options" not in st.session_state:
        st.session_state.options = []
    if "criteria" not in st.session_state:
        # criteria: list of dicts {name: str, weight: float}
        st.session_state.criteria = []
    if "scores" not in st.session_state:
        # scores stored as dict: {option: {criterion: score}}
        st.session_state.scores = {}


init_state()


def parse_options_text(text: str) -> List[str]:
    lines = [l.strip() for l in text.splitlines()]
    return [l for l in lines if l]


# --- UI ---
st.title("Decisions Dashboard 🧭")
st.write(
    "A lightweight Streamlit app to collect options, define criteria with weights, score options, and pick the best choice."
)

# Columns for input
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Add / Import Options")
    new_option = st.text_input("Add a single option", key="new_option_input")
    add_opt = st.button("Add option")
    pasted = st.text_area("Paste newline-separated options")
    uploaded = st.file_uploader("Or upload a CSV (single column of options)", type=["csv", "txt"])

    if add_opt and new_option:
        if new_option not in st.session_state.options:
            st.session_state.options.append(new_option)
            st.session_state.scores[new_option] = {}
            st.success(f"Added option: {new_option}")
        else:
            st.warning("Option already exists")

    if st.button("Import pasted options") and pasted:
        parsed = parse_options_text(pasted)
        added = 0
        for p in parsed:
            if p not in st.session_state.options:
                st.session_state.options.append(p)
                st.session_state.scores[p] = {}
                added += 1
        st.success(f"Imported {added} options")

    if uploaded:
        try:
            df = pd.read_csv(uploaded, header=None)
            # take first column
            col0 = df.iloc[:, 0].astype(str).tolist()
            added = 0
            for p in col0:
                p = p.strip()
                if p and p not in st.session_state.options:
                    st.session_state.options.append(p)
                    st.session_state.scores[p] = {}
                    added += 1
            st.success(f"Imported {added} options from file")
        except Exception as e:
            st.error(f"Failed to read file: {e}")

with col2:
    st.subheader("Current Options")
    if st.session_state.options:
        for opt in list(st.session_state.options):
            cols = st.columns([4, 1, 1])
            cols[0].write(opt)
            if cols[1].button("Remove", key=f"rm_{opt}"):
                st.session_state.options.remove(opt)
                st.session_state.scores.pop(opt, None)
                st.experimental_rerun()
            if cols[2].button("Edit", key=f"edit_{opt}"):
                new_val = st.text_input(f"Rename {opt}", value=opt, key=f"rename_{opt}")
                if st.button("Save", key=f"save_{opt}") and new_val:
                    # rename option in options list and scores
                    idx = st.session_state.options.index(opt)
                    st.session_state.options[idx] = new_val
                    st.session_state.scores[new_val] = st.session_state.scores.pop(opt, {})
                    st.experimental_rerun()
    else:
        st.info("No options yet. Add options on the left.")

st.markdown("---")

# Criteria management
st.subheader("Criteria & Weights")
crit_col1, crit_col2 = st.columns([3, 1])
with crit_col1:
    new_crit = st.text_input("New criterion name", key="new_crit_input")
with crit_col2:
    new_weight = st.number_input("Weight", min_value=0.0, max_value=100.0, value=1.0, step=0.5, key="new_crit_weight")

if st.button("Add criterion") and new_crit:
    if any(c["name"] == new_crit for c in st.session_state.criteria):
        st.warning("Criterion already exists")
    else:
        st.session_state.criteria.append({"name": new_crit, "weight": float(new_weight)})
        # initialize scores for existing options
        for opt in st.session_state.options:
            st.session_state.scores.setdefault(opt, {})
        st.success(f"Added criterion: {new_crit}")

if st.session_state.criteria:
    st.write("Adjust weights (they will be normalized automatically)")
    for i, c in enumerate(st.session_state.criteria):
        cols = st.columns([3, 1, 1])
        cols[0].write(c["name"])
        w = cols[1].number_input("Weight", key=f"w_{i}", value=float(c["weight"]))
        if cols[2].button("Remove", key=f"rmc_{i}"):
            st.session_state.criteria.pop(i)
            st.experimental_rerun()
        else:
            st.session_state.criteria[i]["weight"] = float(w)
else:
    st.info("No criteria defined. You can still pick a random option or define criteria to score options.")

st.markdown("---")

# Scoring interface
st.subheader("Score Options")
if not st.session_state.options:
    st.info("Add options to begin scoring.")
else:
    if not st.session_state.criteria:
        st.write("No criteria defined. Use the 'Random choice' helper below or add criteria to score options.")
        if st.button("Pick a random option"):
            import random

            pick = random.choice(st.session_state.options)
            st.success(f"Random pick: {pick}")
    else:
        # Normalize weights
        total_weight = sum(c["weight"] for c in st.session_state.criteria)
        if total_weight <= 0:
            normalized = [1.0 / len(st.session_state.criteria)] * len(st.session_state.criteria)
        else:
            normalized = [c["weight"] / total_weight for c in st.session_state.criteria]

        # Build scoring UI
        st.write("Use the sliders to score each option for each criterion (0-100).")
        score_container = st.container()
        with score_container:
            for opt in st.session_state.options:
                st.markdown(f"**{opt}**")
                for ci, c in enumerate(st.session_state.criteria):
                    key = f"score_{opt}_{c['name']}"
                    # initialize from session_state.scores if present
                    initial = st.session_state.scores.get(opt, {}).get(c["name"], 50)
                    val = st.slider(c["name"], 0, 100, int(initial), key=key)
                    st.session_state.scores.setdefault(opt, {})[c["name"]] = val

        if st.button("Calculate results"):
            # compute weighted score per option
            rows = []
            for opt in st.session_state.options:
                s = 0.0
                for idx, c in enumerate(st.session_state.criteria):
                    score = float(st.session_state.scores.get(opt, {}).get(c["name"], 0))
                    s += score * normalized[idx]
                rows.append({"option": opt, "score": s})
            results_df = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
            st.session_state.last_results = results_df
            st.success("Results calculated")

# Show results if available
if "last_results" in st.session_state:
    st.markdown("---")
    st.subheader("Results")
    df = st.session_state.last_results
    st.dataframe(df.style.format({"score": "{:.2f}"}))

    # Chart
    chart = alt.Chart(df).mark_bar().encode(x=alt.X("score:Q"), y=alt.Y("option:N", sort="-x"))
    st.altair_chart(chart, use_container_width=True)

    # Export CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download results (CSV)", data=csv, file_name="decision_results.csv", mime="text/csv")

st.markdown("---")
st.write("Tips: Define clear criteria and weights. Use weights to express how important each criterion is relative to others.")

# Footer
st.caption("Created with ❤️ — Decisions Dashboard. Save or export results as needed.")

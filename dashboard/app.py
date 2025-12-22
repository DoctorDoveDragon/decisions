"""
Main Dashboard with Navigation
"""

import streamlit as st
import os
import traceback

# Page configuration
st.set_page_config(
    page_title="Comparative Decision Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2563EB;
        margin-bottom: 1rem;
    }
    .nav-button {
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #3B82F6;
        margin: 0.5rem 0;
        transition: all 0.3s;
    }
    .nav-button:hover {
        background-color: #3B82F6;
        color: white;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #3B82F6;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


def show_home_page():
    """Default home page if module is missing"""
    st.markdown('<h1 class="main-header">🧠 Comparative Decision Intelligence Platform</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 Integrated Understanding System
    
    This platform combines **philosophical wisdom** with **mechanical process analysis**
    to provide comprehensive decision intelligence.
    """)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🏛️ Philosophical Traditions</h3>
            <h2>2+</h2>
            <p>Stoic, Utilitarian, Buddhist</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🔧 Process Dimensions</h3>
            <h2>5</h2>
            <p>Formula, Etymology, Theory, Culture, Utility</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🌐 API Endpoints</h3>
            <h2>10+</h2>
            <p>Analysis, Comparison, Research Tools</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Two main modules
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>🏛️ Philosophical Analysis</h3>
            <p><b>Analyze decisions through:</b></p>
            <ul>
            <li>Stoic virtue ethics</li>
            <li>Utilitarian calculus</li>
            <li>Buddhist mindfulness</li>
            <li>Comparative insights</li>
            </ul>
            <p><b>Features:</b></p>
            <ul>
            <li>✓ Virtue alignment scoring</li>
            <li>✓ Control analysis</li>
            <li>✓ Cross-tradition comparison</li>
            <li>✓ Academic citations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Go to Philosophical Analysis →", key="phil_btn"):
            st.experimental_set_query_params(page="analysis")
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>🔧 Mechanical Process Ontology</h3>
            <p><b>Understand processes through 5 dimensions:</b></p>
            <ol>
            <li><b>Formula</b> - Mathematical representation</li>
            <li><b>Etymology</b> - Historical origins</li>
            <li><b>Theory</b> - Scientific foundation</li>
            <li><b>Culture</b> - Societal interpretation</li>
            <li><b>Utility</b> - Practical application</li>
            </ol>
            <p><b>Example processes:</b></p>
            <ul>
            <li>Entropy</li>
            <li>Diffusion</li>
            <li>Oscillation</li>
            <li>Catalysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Go to Mechanical Processes →", key="mech_btn"):
            st.experimental_set_query_params(page="mechanical_processes")
    
    # Quick start
    st.markdown("""
    ## 🚀 Quick Start
    
    <div class="card">
    <h4>1. Start the platform:</h4>
    ```bash
    # Terminal 1 - API server
    python -m api.server
    
    # Terminal 2 - Dashboard
    streamlit run dashboard/app.py
    ```
    
    <h4>2. Or use the launcher:</h4>
    ```bash
    ./start.sh  # Starts everything
    ```
    
    <h4>3. Open in browser:</h4>
    <ul>
    <li>Dashboard: http://localhost:8501</li>
    <li>API Docs: http://localhost:8000/docs</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


def show_analysis_page():
    """Default philosophical analysis page"""
    st.title("🔍 Philosophical Analysis")
    st.markdown("Analyze decisions through philosophical traditions")
    
    st.markdown("""
    <div class="card">
    <h3>Available Philosophical Traditions:</h3>
    
    <h4>🏛️ Stoicism</h4>
    <p><b>Key principles:</b> Virtue ethics, control dichotomy, resilience</p>
    <p><b>Focus:</b> What's within vs. outside your control</p>
    
    <h4>⚖️ Utilitarianism</h4>
    <p><b>Key principles:</b> Greatest happiness, consequence analysis</p>
    <p><b>Focus:</b> Maximizing overall wellbeing</p>
    
    <h4>☸️ Buddhism (Coming Soon)</h4>
    <p><b>Key principles:</b> Mindfulness, interdependence, non-attachment</p>
    <p><b>Focus:</b> Reducing suffering through wisdom</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Analysis form
    with st.form("decision_analysis"):
        st.subheader("📝 Analyze Your Decision")
        
        decision = st.text_area("Describe your decision:", 
                               placeholder="Should I change careers? Should I invest in this opportunity?")
        
        options = st.text_area("Available options (one per line):",
                              placeholder="Option A\nOption B\nOption C")
        
        tradition = st.selectbox("Philosophical Tradition:", 
                                ["Stoic", "Utilitarian", "Buddhist (Coming Soon)"])
        
        submitted = st.form_submit_button("Analyze Decision", type="primary")
        
        if submitted:
            if decision and options:
                st.success("✅ Analysis complete!")
                st.info("This is a placeholder. Install the full platform for actual analysis.")
            else:
                st.warning("Please fill in both decision description and options")

def show_mechanical_processes_page():
    """Default mechanical processes page"""
    st.title("🔧 Mechanical Process Ontology")
    st.markdown("Understand processes through 5 dimensions")
    
    # Dimension explanations
    dimensions = {
        "📐 Formula": "Mathematical representation and derivation",
        "📜 Etymology": "Linguistic origins and historical evolution",
        "🧪 Theory": "Scientific foundations and philosophical basis",
        "🏛️ Culture": "Societal interpretation and application",
        "⚙️ Utility": "Practical value and implementation"
    }
    
    for name, desc in dimensions.items():
        with st.expander(name):
            st.write(desc)
    
    # Example: Entropy
    st.markdown("""
    <div class="card">
    <h3>🔬 Example: Entropy Analysis</h3>
    
    <h4>📐 Formula:</h4>
    <p>S = k_B ln Ω</p>
    
    <h4>📜 Etymology:</h4>
    <p>Greek: "en-" (within) + "tropē" (transformation) → "inner transformation"</p>
    
    <h4>🧪 Theory:</h4>
    <p>Second Law of Thermodynamics, Statistical Mechanics, Information Theory</p>
    
    <h4>🏛️ Culture:</h4>
    <p>Arrow of time, universal disorder, heat death of universe</p>
    
    <h4>⚙️ Utility:</h4>
    <p>Heat engines, information compression, ecological analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Analyze Entropy Process"):
        st.info("This is a placeholder. Install the full platform for actual process analysis.")

def show_comparative_engine_page():
    """Comparative engine page"""
    st.title("📊 Comparative Engine")
    st.markdown("Cross-tradition comparison and synthesis")
    
    st.markdown("""
    <div class="card">
    <h3>Comparative Analysis Features:</h3>
    
    <h4>🔄 Tradition Comparison</h4>
    <p>Compare Stoic vs. Utilitarian vs. Buddhist perspectives on the same decision</p>
    
    <h4>⚡ Insight Synthesis</h4>
    <p>Generate integrated insights from multiple philosophical traditions</p>
    
    <h4>📈 Decision Scoring</h4>
    <p>Score decisions across multiple ethical dimensions</p>
    
    <h4>🎯 Consensus Finding</h4>
    <p>Identify common ground and divergence between traditions</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Select Traditions to Compare:")
        stoic = st.checkbox("Stoicism", value=True)
        utilitarian = st.checkbox("Utilitarianism", value=True)
        buddhist = st.checkbox("Buddhism", value=False)
    
    with col2:
        st.subheader("Comparison Focus:")
        focus = st.selectbox("Analysis dimension:",
                           ["Ethical principles", "Decision criteria", 
                            "Outcome evaluation", "Virtue development"])
    
    if st.button("Run Comparative Analysis"):
        st.success("✅ Comparative analysis complete!")
        st.info("This is a placeholder. Install the full platform for actual comparison.")

def show_research_tools_page():
    """Research tools page"""
    st.title("📚 Research Tools")
    st.markdown("Academic paper generation and export tools")
    
    st.markdown("""
    <div class="card">
    <h3>Research Features:</h3>
    
    <h4>📄 Paper Templates</h4>
    <ul>
    <li>Philosophical analysis papers</li>
    <li>Mechanical process studies</li>
    <li>Comparative ethics research</li>
    </ul>
    
    <h4>🔬 Analysis Tools</h4>
    <ul>
    <li>Statistical significance testing</li>
    <li>Cross-cultural validation</li>
    <li>Historical trend analysis</li>
    </ul>
    
    <h4>📊 Export Formats</h4>
    <ul>
    <li>LaTeX papers</li>
    <li>Word documents</li>
    <li>Markdown reports</li>
    <li>JSON data dumps</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("research_form"):
        st.subheader("Generate Research Paper")
        
        title = st.text_input("Paper Title:", "Comparative Analysis of Decision Frameworks")
        
        paper_type = st.selectbox("Paper Type:", 
                                 ["Philosophical Analysis", 
                                  "Empirical Study", 
                                  "Literature Review",
                                  "Methodology Paper"])
        
        export_format = st.multiselect("Export Formats:", 
                                      ["LaTeX", "Word", "PDF", "Markdown", "HTML"],
                                      default=["LaTeX"])
        
        submitted = st.form_submit_button("Generate Paper")
        
        if submitted:
            st.success("✅ Research paper generated!")
            st.info("This is a placeholder. Install the full platform for actual paper generation.")

def show_configuration_page():
    """Configuration page"""
    st.title("⚙️ Configuration")
    st.markdown("Platform settings and API configuration")
    
    with st.form("config_form"):
        st.subheader("API Settings")
        
        api_url = st.text_input("API Base URL:", "http://localhost:8000")
        api_timeout = st.number_input("API Timeout (seconds):", 
                                     min_value=5, max_value=60, value=30)
        
        st.subheader("Dashboard Settings")
        theme = st.selectbox("Theme:", ["Light", "Dark", "System"])
        refresh_rate = st.selectbox("Auto-refresh Rate:", 
                                   ["Disabled", "30 seconds", "1 minute", "5 minutes"])
        
        st.subheader("Analysis Settings")
        default_tradition = st.selectbox("Default Philosophical Tradition:", 
                                        ["Stoic", "Utilitarian", "Buddhist"])
        
        show_confidence = st.checkbox("Show confidence scores", value=True)
        show_citations = st.checkbox("Show academic citations", value=True)
        
        submitted = st.form_submit_button("Save Configuration")
        
        if submitted:
            st.success("✅ Configuration saved!")
            st.info("Settings will be applied after restart.")


# --- Helper: robust import-and-run routine ---
def _try_import_and_run(module_name):
    """Try to import decisions.dashboard.pages.<module_name> and run its main().

    Tries absolute import first (for installed package), then relative import (for
    in-repo imports when running as a module). Returns a tuple (ran, error_text).
    If ran is True, the module main() was called. If False, error_text contains
    a combined traceback of the import attempts.
    """
    attempts = []

    # Attempt absolute import (package installed or running as package)
    try:
        mod = __import__(f"decisions.dashboard.pages.{module_name}", fromlist=["*"])
        if hasattr(mod, "main"):
            mod.main()
            return True, None
        else:
            attempts.append(f"Imported decisions.dashboard.pages.{module_name} but no main() found.")
    except Exception:
        attempts.append(traceback.format_exc())

    # Attempt relative import (if this module is itself within a package)
    try:
        mod = __import__(f".pages.{module_name}", globals(), locals(), ["*"])
        if hasattr(mod, "main"):
            mod.main()
            return True, None
        else:
            attempts.append(f"Imported .pages.{module_name} but no main() found.")
    except Exception:
        attempts.append(traceback.format_exc())

    return False, "\n---\n".join(attempts)


def main():
    # --- Sidebar navigation and routing ---
    st.sidebar.title("🧭 Navigation")

    # Map query param values to sidebar labels
    _query_to_label = {
        "home": "🏠 Home",
        "analysis": "🔍 Philosophical Analysis",
        "mechanical_processes": "🔧 Mechanical Processes",
        "comparative_engine": "📊 Comparative Engine",
        "research_tools": "📚 Research Tools",
        "configuration": "⚙️ Configuration",
    }

    sidebar_options = [
        "🏠 Home",
        "🔍 Philosophical Analysis",
        "🔧 Mechanical Processes",
        "📊 Comparative Engine",
        "📚 Research Tools",
        "⚙️ Configuration"
    ]

    # Determine desired default page from query params (if present)
    query_params = st.experimental_get_query_params()
    requested_page = None
    if "page" in query_params:
        raw = query_params.get("page", [""])[0] or ""
        requested_page = _query_to_label.get(raw.lower())

    default_index = 0
    if requested_page in sidebar_options:
        default_index = sidebar_options.index(requested_page)

    page = st.sidebar.radio("Go to", sidebar_options, index=default_index)

    # Page routing: try to import dashboard.pages.* modules first (package-aware),
    # fallback to local implementations when imports are missing or fail.
    if page == "🏠 Home":
        ran, err = _try_import_and_run("home")
        if not ran:
            if err:
                st.error("Home page module import failed; showing built-in home page. Details:\n" + err)
            show_home_page()

    elif page == "🔍 Philosophical Analysis":
        ran, err = _try_import_and_run("analysis")
        if not ran:
            if err:
                st.error("Analysis page module import failed; showing built-in analysis page. Details:\n" + err)
            show_analysis_page()

    elif page == "🔧 Mechanical Processes":
        ran, err = _try_import_and_run("mechanical_processes")
        if not ran:
            if err:
                st.error("Mechanical processes module import failed; showing built-in page. Details:\n" + err)
            show_mechanical_processes_page()

    elif page == "📊 Comparative Engine":
        # Comparative engine handled locally in this file
        show_comparative_engine_page()

    elif page == "📚 Research Tools":
        show_research_tools_page()

    elif page == "⚙️ Configuration":
        show_configuration_page()


if __name__ == "__main__":
    main()

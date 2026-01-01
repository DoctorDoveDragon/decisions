"""
Mechanical Processes Page Module

This module provides a canonical import path for the mechanical processes page.
It loads the original file (3_🧠_Mechanical_Processes.py) and exposes its main() function.
"""

import os
import sys
from importlib.util import spec_from_file_location, module_from_spec
Mechanical Processes Page Module (Canonical Wrapper)

This module provides the canonical import path for the mechanical processes page.
It loads the actual implementation from 3_🧠_Mechanical_Processes.py and exposes the main() function.
"""

import os
import importlib.util

# Get the directory containing this file
_current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the original mechanical processes file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")

# Load the original module using modern importlib API
try:
    if not os.path.exists(_original_file):
        raise FileNotFoundError(
            f"Original mechanical processes file not found: {_original_file}"
        )
    
    _spec = spec_from_file_location("_mechanical_processes_impl", _original_file)
    if _spec is None or _spec.loader is None:
        raise ImportError(
            f"Failed to create module spec for: {_original_file}"
        )
    
    _mechanical_processes_module = module_from_spec(_spec)
    sys.modules[_spec.name] = _mechanical_processes_module
    _spec.loader.exec_module(_mechanical_processes_module)
    
except (FileNotFoundError, ImportError) as e:
    raise ImportError(
        f"Failed to load mechanical processes module: {e}"
    ) from e

# Expose the main() function from the original module
def main():
    """
    Render the Mechanical Processes page.
    This function delegates to the main() function in the original file.
    """
    return _mechanical_processes_module.main()

# Expose other commonly used functions if needed
# Load the actual implementation from the emoji-named file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")

try:
    # Use modern importlib approach (Python 3.4+)
    _spec = importlib.util.spec_from_file_location("_mechanical_processes_impl", _original_file)
    if _spec is None:
        raise ImportError(f"Cannot create module spec from {_original_file}")
    
    _impl = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_impl)
    
    # Expose the main function from the loaded module
    if not hasattr(_impl, 'main'):
        raise AttributeError(f"Module {_original_file} does not have a main() function")
    
    main = _impl.main
except (ImportError, AttributeError, FileNotFoundError) as e:
    raise ImportError(
        f"Failed to load mechanical processes implementation from {_original_file}: {e}"
    ) from e

# Expose any other public functions or attributes if needed
Mechanical Processes Page Module
"""

import streamlit as st
import requests
import json
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

def main():
    st.title("🔧 Mechanical Process Ontology")
    st.markdown("Understand processes through 5 dimensions")
    
    # Initialize session state
    if 'process_analysis' not in st.session_state:
        st.session_state.process_analysis = None
    if 'process_comparison' not in st.session_state:
        st.session_state.process_comparison = None
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_url = st.text_input("API URL", "http://localhost:8000", key="mech_api_url")
        
        st.divider()
        st.header("📊 Process Selection")
        
        # Process categories
        categories = {
            "Thermodynamic": ["entropy", "heat_transfer", "phase_transition"],
            "Mechanical": ["oscillation", "diffusion", "friction"],
            "Information": ["computation", "communication", "encryption"],
            "Biological": ["metabolism", "evolution", "homeostasis"]
        }
        
        selected_category = st.selectbox("Process Category", list(categories.keys()))
        selected_process = st.selectbox("Select Process", categories[selected_category])
        
        st.divider()
        st.header("🔍 Analysis Dimensions")
        
        dimensions = st.multiselect(
            "Dimensions to analyze:",
            ["formula", "etymology", "theory", "culture", "utility"],
            default=["formula", "theory", "utility"]
        )
        
        if st.button("Analyze Process", use_container_width=True):
            with st.spinner(f"Analyzing {selected_process}..."):
                analyze_process(api_url, selected_process, dimensions)
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["🧠 Process Analysis", "🔄 Comparison", "📚 Documentation"])
    
    with tab1:
        display_process_analysis()
    
    with tab2:
        display_process_comparison(api_url)
    
    with tab3:
        display_documentation()

def analyze_process(api_url, process_name, dimensions):
    """Analyze a mechanical process"""
    try:
        response = requests.post(
            f"{api_url}/api/v1/mechanical-processes/analyze",
            json={
                "process_name": process_name,
                "dimensions": dimensions
            },
            timeout=30
        )
        
        if response.status_code == 200:
            st.session_state.process_analysis = response.json()
            st.success(f"✅ {process_name.capitalize()} analysis complete!")
        else:
            st.error(f"API Error: {response.status_code}")
            st.session_state.process_analysis = create_sample_analysis(process_name)
            
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API server")
        st.info("Using sample analysis for demonstration")
        st.session_state.process_analysis = create_sample_analysis(process_name)
    except Exception as e:
        st.error(f"Analysis failed: {str(e)}")
        st.session_state.process_analysis = create_sample_analysis(process_name)

def display_process_analysis():
    """Display process analysis results"""
    if st.session_state.process_analysis is None:
        st.info("👈 Select a process and click 'Analyze Process' to get started")
        return
    
    analysis = st.session_state.process_analysis
    result = analysis.get("result", {})
    process_name = analysis.get("process", "Unknown").capitalize()
    
    # Header with process info
    st.header(f"🔬 {process_name} Analysis")
    
    # Dimensional profile visualization
    if "dimensional_profile" in result:
        st.subheader("📊 Dimensional Understanding Profile")
        
        profile_data = []
        for dim, score in result["dimensional_profile"].items():
            profile_data.append({
                "Dimension": dim.capitalize(),
                "Score": score,
                "Color": get_dimension_color(dim)
            })
        
        df = pd.DataFrame(profile_data)
        
        # Create radar chart
        fig = go.Figure(data=go.Scatterpolar(
            r=df["Score"],
            theta=df["Dimension"],
            fill='toself',
            line_color='blue',
            marker_color='blue'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            showlegend=False,
            title="5-Dimensional Understanding"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Display each dimension
    dimensions_to_show = [d for d in ["formula", "etymology", "theory", "culture", "utility"] 
                         if d in result and result[d]]
    
    if dimensions_to_show:
        st.subheader("🔍 Dimension Analysis")
        
        for dimension in dimensions_to_show:
            with st.expander(f"📐 {dimension.capitalize()} Dimension", expanded=(dimension=="formula")):
                display_dimension(dimension, result[dimension])
    
    # Synthesis insights
    if "synthesis" in result and result["synthesis"]:
        st.subheader("💡 Synthetic Insights")
        
        insights = result["synthesis"][:5]  # Show top 5 insights
        for i, insight in enumerate(insights, 1):
            st.markdown(f"""
            <div style="background-color: #f0f9ff; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #3B82F6;">
            <strong>Insight {i}:</strong> {insight}
            </div>
            """, unsafe_allow_html=True)

def display_dimension(dimension: str, data: dict):
    """Display a specific dimension's analysis"""
    if dimension == "formula":
        if "symbolic" in data:
            st.latex(data["symbolic"])
        
        if "variables" in data:
            st.markdown("**Variables:**")
            for var, meaning in data["variables"].items():
                st.write(f"  - **{var}**: {meaning}")
        
        if "derivation" in data and data["derivation"]:
            with st.expander("Derivation Steps"):
                for step in data["derivation"]:
                    st.write(f"• {step}")
    
    elif dimension == "etymology":
        if "term" in data:
            st.markdown(f"**Term:** `{data['term']}`")
        
        if "root_words" in data:
            st.markdown("**Root words:**")
            for root in data["root_words"]:
                st.write(f"  - {root}")
        
        if "historical_evolution" in data:
            st.markdown("**Historical evolution:**")
            for era, meaning in data["historical_evolution"]:
                st.write(f"  - **{era}**: {meaning}")
    
    elif dimension == "theory":
        if "theory_name" in data:
            st.markdown(f"**Theory:** {data['theory_name']}")
        
        if "key_principles" in data:
            st.markdown("**Key principles:**")
            for principle in data["key_principles"]:
                st.write(f"  - {principle}")
        
        if "founding_theorists" in data:
            st.markdown("**Founding theorists:**")
            for theorist, contribution in data["founding_theorists"]:
                st.write(f"  - **{theorist}**: {contribution}")
    
    elif dimension == "culture":
        col1, col2 = st.columns(2)
        
        with col1:
            if "mythological_interpretations" in data:
                st.markdown("**Mythological interpretations:**")
                for myth in data["mythological_interpretations"][:3]:
                    st.write(f"• {myth}")
            
            if "artistic_representations" in data:
                st.markdown("**Artistic representations:**")
                for art in data["artistic_representations"][:2]:
                    st.write(f"• {art}")
        
        with col2:
            if "proverbial_wisdom" in data:
                st.markdown("**Proverbial wisdom:**")
                for proverb in data["proverbial_wisdom"][:3]:
                    st.write(f"» \"{proverb}\"")
            
            if "rituals" in data:
                st.markdown("**Cultural rituals:**")
                for ritual in data["rituals"][:2]:
                    st.write(f"• {ritual}")
    
    elif dimension == "utility":
        if "primary_applications" in data:
            st.markdown("**Primary applications:**")
            for app in data["primary_applications"][:5]:
                st.write(f"  - {app}")
        
        if "innovation_potential" in data:
            st.markdown("**Innovation potential:**")
            for innovation in data["innovation_potential"][:3]:
                st.write(f"  - {innovation}")
        
        if "efficiency_metrics" in data:
            st.markdown("**Efficiency metrics:**")
            for metric, value in data["efficiency_metrics"].items():
                st.write(f"  - **{metric}**: {value}")

def display_process_comparison(api_url):
    """Display process comparison interface"""
    st.header("🔄 Process Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        process1 = st.selectbox(
            "First Process",
            ["entropy", "diffusion", "oscillation", "heat_transfer"],
            key="compare_process1"
        )
    
    with col2:
        process2 = st.selectbox(
            "Second Process",
            ["diffusion", "entropy", "oscillation", "heat_transfer"],
            index=1,
            key="compare_process2"
        )
    
    if st.button("Compare Processes", type="primary", use_container_width=True):
        if process1 == process2:
            st.warning("Please select two different processes")
            return
        
        with st.spinner(f"Comparing {process1} vs {process2}..."):
            compare_processes(api_url, process1, process2)

def compare_processes(api_url, process1, process2):
    """Compare two processes"""
    try:
        response = requests.post(
            f"{api_url}/api/v1/mechanical-processes/compare",
            json={
                "process1": process1,
                "process2": process2
            },
            timeout=30
        )
        
        if response.status_code == 200:
            st.session_state.process_comparison = response.json()
            display_comparison_results()
        else:
            st.error(f"Comparison failed: {response.status_code}")
            
    except Exception as e:
        st.error(f"Comparison error: {str(e)}")
        st.session_state.process_comparison = create_sample_comparison(process1, process2)
        display_comparison_results()

def display_comparison_results():
    """Display comparison results"""
    if st.session_state.process_comparison is None:
        return
    
    comparison = st.session_state.process_comparison
    result = comparison.get("result", {})
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤝 Similarities")
        similarities = result.get("similarities", [])
        if similarities:
            for similarity in similarities[:5]:
                st.success(f"• {similarity}")
        else:
            st.info("No significant similarities found")
    
    with col2:
        st.subheader("⚡ Differences")
        differences = result.get("differences", [])
        if differences:
            for difference in differences[:5]:
                st.warning(f"• {difference}")
        else:
            st.info("No significant differences found")
    
    st.divider()
    
    # Connections
    if "connections" in result and result["connections"]:
        st.subheader("🔗 Conceptual Connections")
        for connection in result["connections"]:
            st.info(f"• {connection}")
    
    # Comparative insights
    if "comparative_insights" in result and result["comparative_insights"]:
        st.subheader("💡 Comparative Insights")
        for insight in result["comparative_insights"]:
            st.markdown(f"""
            <div style="background-color: #f0f9ff; padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            {insight}
            </div>
            """, unsafe_allow_html=True)

def display_documentation():
    """Display documentation for mechanical process ontology"""
    st.header("📚 Mechanical Process Ontology Documentation")
    
    st.markdown("""
    ## The 5-Dimensional Framework
    
    This framework analyzes mechanical processes through five complementary dimensions:
    """)
    
    dimensions_info = [
        {
            "dimension": "📐 Formula",
            "description": "Mathematical representation and derivation",
            "focus": "Quantitative relationships, variables, assumptions, domain",
            "example": "F = ma, S = k ln Ω, E = mc²"
        },
        {
            "dimension": "📜 Etymology", 
            "description": "Linguistic and historical origins of terms",
            "focus": "Word evolution, root meanings, conceptual history",
            "example": "'Entropy' from Greek 'en-' (within) + 'tropē' (transformation)"
        },
        {
            "dimension": "🧪 Theory",
            "description": "Scientific and philosophical foundations",
            "focus": "Key principles, founding theorists, historical context",
            "example": "Second Law of Thermodynamics, Statistical Mechanics"
        },
        {
            "dimension": "🏛️ Culture",
            "description": "Societal interpretations and applications",
            "focus": "Mythology, religion, art, proverbs, social norms",
            "example": "Entropy as 'arrow of time' in cultural narratives"
        },
        {
            "dimension": "⚙️ Utility",
            "description": "Practical applications and value creation",
            "focus": "Applications, efficiency, cost-benefit, innovation",
            "example": "Heat engines, information compression, ecological analysis"
        }
    ]
    
    for info in dimensions_info:
        with st.expander(info["dimension"]):
            st.markdown(f"""
            **Description:** {info["description"]}
            
            **Focus:** {info["focus"]}
            
            **Example:** {info["example"]}
            """)

def get_dimension_color(dimension: str) -> str:
    """Get color for dimension visualization"""
    colors = {
        "formula": "#3B82F6",    # Blue
        "etymology": "#10B981",  # Green
        "theory": "#8B5CF6",     # Purple
        "culture": "#F59E0B",    # Amber
        "utility": "#EF4444"     # Red
    }
    return colors.get(dimension, "#6B7280")

def create_sample_analysis(process_name: str) -> dict:
    """Create sample analysis for demonstration"""
    sample_data = {
        "entropy": {
            "process": "entropy",
            "result": {
                "category": "thermodynamic",
                "formula": {
                    "symbolic": "S = k_B \\ln \\Omega",
                    "variables": {
                        "S": "Entropy (measure of disorder)",
                        "k_B": "Boltzmann constant",
                        "Ω": "Number of microstates",
                        "T": "Temperature"
                    },
                    "derivation": [
                        "Clausius definition: dS = δQ_rev/T",
                        "Boltzmann statistical: S = k_B ln Ω",
                        "Shannon information: H = -Σ p_i log p_i"
                    ]
                },
                "dimensional_profile": {
                    "formula": 0.9,
                    "etymology": 0.7,
                    "theory": 0.85,
                    "culture": 0.6,
                    "utility": 0.8
                },
                "synthesis": [
                    "Entropy reveals universal tendency toward disorder",
                    "Information and thermodynamic entropy are fundamentally connected",
                    "Life represents local entropy decrease powered by global increase"
                ]
            }
        }
    }
    
    return sample_data.get(process_name, {
        "process": process_name,
        "result": {
            "category": "general",
            "dimensional_profile": {
                "formula": 0.5,
                "etymology": 0.5,
                "theory": 0.5,
                "culture": 0.5,
                "utility": 0.5
            },
            "synthesis": ["Process analysis available in full version"]
        }
    })

def create_sample_comparison(process1: str, process2: str) -> dict:
    """Create sample comparison for demonstration"""
    return {
        "processes": [process1, process2],
        "result": {
            "similarities": [
                "Both processes involve state transformations",
                "Mathematical models exist for both phenomena",
                "Both have thermodynamic implications"
            ],
            "differences": [
                f"{process1} focuses on disorder, {process2} focuses on spatial distribution",
                f"Different mathematical formalizations",
                f"Distinct cultural interpretations"
            ],
            "connections": [
                f"{process1} and {process2} often co-occur in natural systems",
                "Both can be analyzed using statistical mechanics"
            ],
            "comparative_insights": [
                f"Understanding both {process1} and {process2} provides comprehensive view of system behavior",
                "Combined analysis reveals emergent properties"
            ]
        }
    }

if __name__ == "__main__":
    main()
Mechanical Processes page - wrapper for the emoji-named file.
"""

# Import from the emoji-named file
from importlib import import_module

# Import the actual module
_emoji_module = import_module("dashboard.pages.3_🧠_Mechanical_Processes")

# Re-export the main function
main = _emoji_module.main

__all__ = ["main"]

"""
Dashboard Page for Mechanical Process Analysis
"""

import streamlit as st
import requests
import json
from typing import Dict, Any, List
import plotly.graph_objects as go
import pandas as pd

def main():
    st.set_page_config(
        page_title="Mechanical Process Analysis",
        page_icon="🔧",
        layout="wide"
    )
    
    st.title("🔧 Mechanical Process Ontology")
    st.markdown("""
    Understand mechanical processes through **5 dimensions**:
    1. **Formula** - Mathematical representation
    2. **Etymology** - Linguistic/historical origins  
    3. **Theory** - Scientific/philosophical foundation
    4. **Culture** - Societal interpretation
    5. **Utility** - Practical application/value
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_url = st.text_input("API URL", "http://localhost:8000")
        
        st.divider()
        
        st.header("📊 Process Selection")
        process_category = st.selectbox(
            "Process Category",
            ["thermodynamic", "mechanical", "electromagnetic", 
             "chemical", "biological", "information", "social", "cognitive"],
            index=0
        )
        
        # Get available processes (would need API endpoint)
        available_processes = ["entropy", "diffusion", "oscillation", "catalysis"]
        selected_process = st.selectbox("Select Process", available_processes)
        
        analysis_dimensions = st.multiselect(
            "Analysis Dimensions",
            ["formula", "etymology", "theory", "culture", "utility"],
            default=["formula", "theory", "utility"]
        )
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔬 Process Analysis")
        
        if st.button("Analyze Process", type="primary"):
            analyze_process(api_url, selected_process, analysis_dimensions)
        
        # Comparison section
        st.divider()
        st.subheader("🔄 Process Comparison")
        
        col1a, col1b = st.columns(2)
        with col1a:
            compare_process1 = st.selectbox("Process 1", available_processes, index=0)
        with col1b:
            compare_process2 = st.selectbox("Process 2", available_processes, index=1)
        
        if st.button("Compare Processes"):
            compare_processes(api_url, compare_process1, compare_process2)
    
    with col2:
        st.subheader("📈 Dimensional Analysis")
        
        # Sample dimensional profile visualization
        st.markdown("""
        **5-Dimensional Profile:**
        
        ```python
        Formula:      ████████░░ 0.8
        Etymology:    █████░░░░░ 0.5  
        Theory:       ████████░░ 0.8
        Culture:      ████░░░░░░ 0.4
        Utility:      █████████░ 0.9
        ```
        """)
        
        st.divider()
        
        st.subheader("🔗 Quick Links")
        st.markdown("""
        - [Entropy Analysis](/entropy)
        - [Process Categories](/categories)
        - [Cross-Connections](/connections)
        - [API Documentation](/docs)
        """)

def analyze_process(api_url: str, process_name: str, dimensions: List[str]):
    """Analyze a mechanical process"""
    with st.spinner(f"Analyzing {process_name}..."):
        try:
            response = requests.post(
                f"{api_url}/api/v1/mechanical-processes/analyze",
                json={
                    "process_name": process_name,
                    "dimensions": dimensions
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                display_analysis(result)
            else:
                st.error(f"API Error: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to API server")
            st.info("Make sure the API is running: `python -m api.server`")
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")

def display_analysis(analysis: Dict[str, Any]):
    """Display process analysis results"""
    result = analysis.get("result", {})
    process_name = analysis.get("process", "Unknown")
    
    st.success(f"✅ Analysis complete for {process_name}")
    
    # Dimensional profile visualization
    if "dimensional_profile" in result:
        st.subheader("📊 Dimensional Profile")
        
        profile = result["dimensional_profile"]
        df = pd.DataFrame([
            {"Dimension": dim, "Score": score}
            for dim, score in profile.items()
        ])
        
        # Create bar chart
        fig = go.Figure(data=[
            go.Bar(
                x=df["Dimension"],
                y=df["Score"],
                marker_color='lightblue'
            )
        ])
        fig.update_layout(
            title="5-Dimensional Understanding Score",
            yaxis_title="Score (0-1)",
            yaxis_range=[0, 1]
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Display selected dimensions
    st.subheader("🔍 Analysis Results")
    
    tabs = st.tabs([dim.capitalize() for dim in analysis.get("result", {}).keys() 
                    if dim in ["formula", "etymology", "theory", "culture", "utility"]])
    
    for i, (dim_name, dim_data) in enumerate(result.items()):
        if dim_name in ["formula", "etymology", "theory", "culture", "utility"]:
            with tabs[i]:
                display_dimension(dim_name, dim_data)
    
    # Synthesis insights
    if "synthesis" in result:
        st.subheader("💡 Synthetic Insights")
        for insight in result["synthesis"][:5]:  # Top 5 insights
            st.info(f"• {insight}")

def display_dimension(dimension: str, data: Dict[str, Any]):
    """Display a specific dimension's analysis"""
    if dimension == "formula":
        st.markdown(f"**Formula:** ${data.get('symbolic', '')}$")
        st.markdown("**Variables:**")
        for var, meaning in data.get("variables", {}).items():
            st.write(f"  - {var}: {meaning}")
    
    elif dimension == "etymology":
        st.markdown(f"**Term:** {data.get('term', '')}")
        st.markdown(f"**Origin:** {data.get('language_origin', '')}")
        st.markdown("**Historical Evolution:**")
        for era, meaning in data.get("historical_evolution", []):
            st.write(f"  - {era}: {meaning}")
    
    elif dimension == "theory":
        st.markdown(f"**Theory:** {data.get('theory_name', '')}")
        st.markdown("**Key Principles:**")
        for principle in data.get("key_principles", []):
            st.write(f"  - {principle}")
    
    elif dimension == "culture":
        st.markdown("**Cultural Interpretations:**")
        for myth in data.get("mythological_interpretations", []):
            st.write(f"  - {myth}")
        
        st.markdown("**Proverbial Wisdom:**")
        for proverb in data.get("proverbial_wisdom", []):
            st.write(f"  - \"{proverb}\"")
    
    elif dimension == "utility":
        st.markdown("**Primary Applications:**")
        for app in data.get("primary_applications", []):
            st.write(f"  - {app}")
        
        st.markdown("**Innovation Potential:**")
        for innovation in data.get("innovation_potential", []):
            st.write(f"  - {innovation}")

def compare_processes(api_url: str, process1: str, process2: str):
    """Compare two processes"""
    with st.spinner(f"Comparing {process1} vs {process2}..."):
        try:
            response = requests.post(
                f"{api_url}/api/v1/mechanical-processes/compare",
                json={
                    "process1": process1,
                    "process2": process2
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                display_comparison(result)
            else:
                st.error(f"API Error: {response.status_code}")
                
        except Exception as e:
            st.error(f"Comparison failed: {str(e)}")

def display_comparison(comparison: Dict[str, Any]):
    """Display process comparison results"""
    result = comparison.get("result", {})
    
    st.success("✅ Comparison complete")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤝 Similarities")
        for similarity in result.get("similarities", []):
            st.info(f"• {similarity}")
    
    with col2:
        st.subheader("⚡ Differences")
        for difference in result.get("differences", []):
            st.warning(f"• {difference}")
    
    st.subheader("🔗 Connections")
    for connection in result.get("connections", []):
        st.write(f"• {connection}")
    
    st.subheader("💡 Comparative Insights")
    for insight in result.get("comparative_insights", []):
        st.success(f"• {insight}")

if __name__ == "__main__":
    main()

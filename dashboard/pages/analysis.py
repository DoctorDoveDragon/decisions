"""
Philosophical Analysis Page Module
"""

import streamlit as st
import requests
import json
from datetime import datetime

def main():
    st.title("🔍 Philosophical Decision Analysis")
    st.markdown("Analyze decisions through philosophical traditions")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_url = st.text_input("API URL", "http://localhost:8000")
        
        st.divider()
        st.header("📋 Quick Templates")
        
        templates = {
            "Career Change": {
                "description": "Should I leave my stable job to start a business?",
                "options": ["Stay in current job", "Start business part-time", "Start business full-time"],
                "stakeholders": ["Myself", "Family", "Current employer", "Future customers"]
            },
            "Ethical Dilemma": {
                "description": "A colleague is taking credit for my work. What should I do?",
                "options": ["Confront directly", "Report to manager", "Document and wait", "Let it go"],
                "stakeholders": ["Myself", "Colleague", "Manager", "Team"]
            },
            "Investment Decision": {
                "description": "Should I invest in this new technology startup?",
                "options": ["Invest $10,000", "Invest $5,000", "Do not invest", "Wait 6 months"],
                "stakeholders": ["Myself", "Family", "Startup team", "Other investors"]
            }
        }
        
        selected_template = st.selectbox("Choose a template:", list(templates.keys()))
        
        if st.button("Load Template"):
            template = templates[selected_template]
            st.session_state.template_description = template["description"]
            st.session_state.template_options = "\n".join(template["options"])
            st.session_state.template_stakeholders = template["stakeholders"]
            st.rerun()
    
    # Main analysis form
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Decision Context")
        
        description = st.text_area(
            "Decision Description:",
            value=getattr(st.session_state, 'template_description', ''),
            height=150,
            placeholder="Describe the decision you need to make..."
        )
        
        options = st.text_area(
            "Available Options (one per line):",
            value=getattr(st.session_state, 'template_options', 'Option A\nOption B'),
            height=100,
            placeholder="Option A\nOption B\nOption C"
        )
        
        stakeholders = st.text_area(
            "Affected Stakeholders (comma-separated):",
            value=", ".join(getattr(st.session_state, 'template_stakeholders', ["Myself", "Others"])),
            placeholder="Myself, Family, Colleagues, Community"
        )
    
    with col2:
        st.subheader("🏛️ Philosophical Tradition")
        
        tradition = st.radio(
            "Select tradition:",
            ["Stoic", "Utilitarian", "Buddhist (Coming Soon)"],
            index=0
        )
        
        st.divider()
        
        st.subheader("🎯 Analysis Parameters")
        
        include_confidence = st.checkbox("Include confidence scores", value=True)
        include_citations = st.checkbox("Include academic citations", value=False)
        compare_traditions = st.checkbox("Compare with other traditions", value=False)
    
    if st.button("🔍 Analyze Decision", type="primary", use_container_width=True):
        if not description.strip():
            st.error("Please provide a decision description")
            return
            
        options_list = [opt.strip() for opt in options.split('\n') if opt.strip()]
        if len(options_list) < 2:
            st.error("Please provide at least two options")
            return
        
        analyze_decision(api_url, tradition, description, options_list, stakeholders)

def analyze_decision(api_url, tradition, description, options, stakeholders):
    """Call API to analyze decision"""
    with st.spinner(f"Analyzing with {tradition} tradition..."):
        try:
            # Prepare request data
            request_data = {
                "description": description,
                "options": options,
                "stakeholders": [s.strip() for s in stakeholders.split(',')] if stakeholders else ["Yourself", "Others"],
                "tradition": tradition.lower().replace(" (coming soon)", ""),
                "user_profile": None
            }
            
            # Call API
            response = requests.post(
                f"{api_url}/analyze",
                json=request_data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                display_results(result, tradition)
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Cannot connect to API server")
            st.info("""
            **Troubleshooting steps:**
            1. Make sure the API server is running: `python -m api.server`
            2. Check the API URL in the sidebar
            3. Verify network connectivity
            """)
            
            # Show sample results for demo
            if st.checkbox("Show sample analysis for demonstration"):
                show_sample_analysis(description, options, tradition)
                
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")

def display_results(result, tradition):
    """Display analysis results"""
    st.success(f"✅ {tradition} Analysis Complete!")
    
    # Decision metadata
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tradition", tradition)
    with col2:
        confidence = result.get("confidence", 0)
        st.metric("Confidence", f"{confidence:.0%}")
    with col3:
        decision_id = result.get("decision_id", "N/A")
        st.metric("Analysis ID", decision_id[:10] + "...")
    
    st.divider()
    
    # Insights
    st.subheader("💡 Key Insights")
    insights = result.get("insights", [])
    for i, insight in enumerate(insights, 1):
        st.info(f"**{i}.** {insight}")
    
    st.divider()
    
    # Recommendations
    st.subheader("🎯 Recommendations")
    recommendations = result.get("recommendations", [])
    for i, recommendation in enumerate(recommendations, 1):
        st.success(f"**{i}.** {recommendation}")
    
    st.divider()
    
    # Additional information
    with st.expander("📊 Detailed Analysis"):
        st.json(result)
        
        # Export options
        st.subheader("📤 Export Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Export as JSON"):
                st.download_button(
                    label="Download JSON",
                    data=json.dumps(result, indent=2),
                    file_name=f"decision_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        with col2:
            if st.button("📋 Copy to Clipboard"):
                st.code(json.dumps(result, indent=2))
                st.success("Copied to clipboard!")
        
        with col3:
            if st.button("📧 Email Report"):
                st.info("Email functionality coming soon")

def show_sample_analysis(description, options, tradition):
    """Show sample analysis when API is not available"""
    st.warning("⚠️ Showing sample analysis (API not connected)")
    
    sample_insights = {
        "Stoic": [
            "Focus on what is within your control",
            "Practice the dichotomy of control",
            "Maintain equanimity regardless of outcomes",
            "View challenges as opportunities for growth"
        ],
        "Utilitarian": [
            "Calculate net happiness for all affected",
            "Consider both short-term and long-term consequences",
            "Weigh stakeholder impacts proportionally",
            "Minimize suffering while maximizing wellbeing"
        ],
        "Buddhist": [
            "Practice mindfulness in decision-making",
            "Consider interdependence of all beings",
            "Let go of attachment to specific outcomes",
            "Act with compassion for all stakeholders"
        ]
    }
    
    sample_recommendations = {
        "Stoic": [
            "Identify what you can and cannot control",
            "Ask: 'What would a wise person do?'",
            "Prepare for all possible outcomes",
            "Focus on developing virtue rather than outcomes"
        ],
        "Utilitarian": [
            "Calculate utility scores for each option",
            "Consider marginalized stakeholders",
            "Account for uncertainty in predictions",
            "Choose option with greatest net benefit"
        ],
        "Buddhist": [
            "Meditate on the decision with mindfulness",
            "Consider karmic implications",
            "Act with right intention and right action",
            "Accept impermanence of all outcomes"
        ]
    }
    
    # Display sample results
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tradition", tradition)
    with col2:
        st.metric("Confidence", "85%")
    with col3:
        st.metric("Analysis ID", "sample_001")
    
    st.divider()
    
    st.subheader("💡 Sample Insights")
    for insight in sample_insights.get(tradition, []):
        st.info(f"• {insight}")
    
    st.divider()
    
    st.subheader("🎯 Sample Recommendations")
    for recommendation in sample_recommendations.get(tradition, []):
        st.success(f"→ {recommendation}")

if __name__ == "__main__":
    main()

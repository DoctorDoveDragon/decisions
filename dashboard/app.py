"""
Main Dashboard with Navigation
"""

import streamlit as st

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
</style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "🔍 Philosophical Analysis", 
        "🔧 Mechanical Processes",
        "📊 Comparative Engine",
        "📚 Research Tools"
    ]
)

# Page routing
if page == "🏠 Home":
    import pages.home
    pages.home.main()
    
elif page == "🔍 Philosophical Analysis":
    import pages.analysis
    pages.analysis.main()
    
elif page == "🔧 Mechanical Processes":
    import pages.mechanical_processes
    pages.mechanical_processes.main()
    
elif page == "📊 Comparative Engine":
    st.title("Comparative Engine")
    st.write("Cross-tradition comparison tools coming soon...")
    
elif page == "📚 Research Tools":
    st.title("Research Tools")
    st.write("Academic paper generation and export coming soon...")

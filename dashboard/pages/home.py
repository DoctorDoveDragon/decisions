"""
Home Page
"""

import streamlit as st

def main():
    st.markdown('<h1 class="main-header">🧠 Comparative Decision Intelligence Platform</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🎯 Integrated Understanding System
    
    This platform combines **philosophical wisdom** with **mechanical process analysis**
    to provide comprehensive decision intelligence.
    """)
    
    # Two main modules
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏛️ Philosophical Analysis")
        st.markdown("""
        **Analyze decisions through:**
        - Stoic virtue ethics
        - Utilitarian calculus  
        - Buddhist mindfulness
        - Comparative insights
        
        **Features:**
        ✓ Virtue alignment scoring
        ✓ Control analysis
        ✓ Cross-tradition comparison
        ✓ Academic citations
        """)
        
        if st.button("Go to Philosophical Analysis →"):
            st.switch_page("pages/analysis.py")
    
    with col2:
        st.subheader("🔧 Mechanical Process Ontology")
        st.markdown("""
        **Understand processes through 5 dimensions:**
        1. **Formula** - Mathematical representation
        2. **Etymology** - Historical origins
        3. **Theory** - Scientific foundation  
        4. **Culture** - Societal interpretation
        5. **Utility** - Practical application
        
        **Example processes:**
        • Entropy • Diffusion • Oscillation • Catalysis
        """)
        
        if st.button("Go to Mechanical Processes →"):
            st.switch_page("pages/mechanical_processes.py")
    
    st.divider()
    
    # Quick start
    st.subheader("🚀 Quick Start")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        **1. Start the platform:**
        ```bash
        # Terminal 1 - API server
        python -m api.server
        
        # Terminal 2 - Dashboard  
        streamlit run dashboard/app.py
        ```
        """)
    
    with col4:
        st.markdown("""
        **2. Or use the launcher:**
        ```bash
        ./start.sh  # Starts everything
        ```
        
        **3. Open in browser:**
        - Dashboard: http://localhost:8501
        - API Docs: http://localhost:8000/docs
        """)
    
    st.divider()
    
    # Architecture diagram
    st.subheader("🏗️ System Architecture")
    
    st.markdown("""
    ```
    ┌─────────────────────────────────────────────────────────┐
    │                    USER INTERFACE                        │
    │  • Philosophical decision analysis                       │
    │  • Mechanical process understanding                     │
    │  • Comparative insights generation                       │
    └───────────────────────┬─────────────────────────────────┘
                            │
    ┌───────────────────────┼─────────────────────────────────┐
    │              CORE ANALYSIS ENGINES                      │
    │  ┌─────────────────┐ ┌─────────────────┐               │
    │  │  PHILOSOPHICAL  │ │   MECHANICAL    │               │
    │  │    ANALYZERS    │ │    PROCESSES    │               │
    │  │  • Stoic        │ │  • Formula      │               │
    │  │  • Utilitarian  │ │  • Etymology    │               │
    │  │  • Buddhist     │ │  • Theory       │               │
    │  │                 │ │  • Culture      │               │
    │  │                 │ │  • Utility      │               │
    │  └─────────────────┘ └─────────────────┘               │
    └───────────────────────┬─────────────────────────────────┘
                            │
    ┌───────────────────────┼─────────────────────────────────┐
    │               KNOWLEDGE BASES                          │
    │  • Philosophical principles & citations                │
    │  • Mathematical formulas & derivations                 │
    │  • Historical etymology & evolution                    │
    │  • Cultural interpretations & applications             │
    └─────────────────────────────────────────────────────────┘
    ```
    """)

if __name__ == "__main__":
    main()

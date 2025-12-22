"""
Home Page Module
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
        
        if st.button("Go to Philosophical Analysis →", key="phil_btn_home"):
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
        
        if st.button("Go to Mechanical Processes →", key="mech_btn_home"):
            st.experimental_set_query_params(page="mechanical_processes")
    
    st.divider()
    
    # Quick start
    st.subheader("🚀 Quick Start")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="card">
        <h4>1. Start the platform:</h4>
        ```bash
        # Terminal 1 - API server
        python -m api.server
        
        # Terminal 2 - Dashboard
        streamlit run dashboard/app.py
        ```
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="card">
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
    
    st.divider()
    
    # Architecture diagram
    st.subheader("🏗️ System Architecture")
    
    st.markdown("""
    ```mermaid
    graph TD
        A[User Interface] --> B[Philosophical Analysis]
        A --> C[Mechanical Processes]
        B --> D[Stoic Analyzer]
        B --> E[Utilitarian Analyzer]
        B --> F[Buddhist Analyzer]
        C --> G[Formula Dimension]
        C --> H[Etymology Dimension]
        C --> I[Theory Dimension]
        C --> J[Culture Dimension]
        C --> K[Utility Dimension]
        D --> L[Comparative Engine]
        E --> L
        F --> L
        G --> M[Knowledge Base]
        H --> M
        I --> M
        J --> M
        K --> M
        L --> N[Integrated Insights]
        M --> N
    ```
    """)
    
    # Features table
    st.subheader("📋 Platform Features")
    
    features = [
        ["Feature", "Philosophical Analysis", "Mechanical Processes"],
        ["Real-time analysis", "✅", "✅"],
        ["Multiple traditions", "✅ (Stoic, Utilitarian, Buddhist)", "✅ (5 Dimensions)"],
        ["Comparative insights", "✅", "✅"],
        ["API access", "✅", "✅"],
        ["Export capabilities", "✅", "✅"],
        ["Academic citations", "✅", "✅"],
        ["Visualization", "✅", "✅"]
    ]
    
    import pandas as pd
    df = pd.DataFrame(features[1:], columns=features[0])
    st.dataframe(df, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()

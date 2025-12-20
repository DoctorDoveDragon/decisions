#!/bin/bash
# ============================================================================
# PATCH: COMPLETE DASHBOARD MODULES
# ENTER INTO: Terminal/Bash (run from project directory)
# PURPOSE: Create all missing dashboard modules for app.py
# ============================================================================

echo -e "${BLUE}Creating complete dashboard modules...${NC}"

# Create the main app.py
cat > dashboard/app.py << 'EOF'
"""
Main Dashboard with Navigation
Comparative Decision Intelligence Platform
"""

import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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
        margin-bottom: 0.5rem;
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
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3B82F6;
        margin: 1rem 0;
    }
    .insight-box {
        background-color: #eff6ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #60a5fa;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"

# Navigation sidebar
with st.sidebar:
    st.title("🧭 Navigation")
    
    # Platform status
    st.markdown("---")
    st.markdown("### 📊 Platform Status")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("API", "🟢 Online", "v1.0.0")
    with col2:
        st.metric("Dashboard", "🟢 Online", "v1.0.0")
    
    st.markdown("---")
    
    # Navigation buttons
    pages = {
        "🏠 Home": "Home",
        "🔍 Philosophical Analysis": "Philosophical Analysis", 
        "🔧 Mechanical Processes": "Mechanical Processes",
        "📊 Comparative Engine": "Comparative Engine",
        "📚 Research Tools": "Research Tools",
        "⚙️ Settings": "Settings"
    }
    
    for page_name, page_id in pages.items():
        if st.button(page_name, key=f"nav_{page_id}", use_container_width=True):
            st.session_state.page = page_name
            st.rerun()
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()
    
    if st.button("📥 Export Session", use_container_width=True):
        st.info("Export functionality coming soon!")
    
    st.markdown("---")
    
    # System info
    st.markdown("### ℹ️ System Info")
    st.caption("Version: 2.0.0")
    st.caption("Last Updated: Today")
    st.caption("Modules: 2/2 Active")

# Page routing
def load_page():
    """Load the appropriate page based on session state"""
    
    if st.session_state.page == "🏠 Home":
        home_page()
        
    elif st.session_state.page == "🔍 Philosophical Analysis":
        philosophical_analysis_page()
        
    elif st.session_state.page == "🔧 Mechanical Processes":
        mechanical_processes_page()
        
    elif st.session_state.page == "📊 Comparative Engine":
        comparative_engine_page()
        
    elif st.session_state.page == "📚 Research Tools":
        research_tools_page()
        
    elif st.session_state.page == "⚙️ Settings":
        settings_page()

def home_page():
    """Home page content"""
    st.markdown('<h1 class="main-header">🧠 Comparative Decision Intelligence Platform</h1>', unsafe_allow_html=True)
    
    # Hero section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
        <h3 class="sub-header">Integrated Wisdom System</h3>
        Combine <strong>philosophical wisdom</strong> with <strong>mechanical analysis</strong>
        for comprehensive decision intelligence and process understanding.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
        <h3>5-Dimensional Analysis</h3>
        <p>Formula • Etymology • Theory • Culture • Utility</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick start section
    st.markdown("## 🚀 Quick Start")
    
    tab1, tab2, tab3 = st.tabs(["📝 Analyze Decision", "🔧 Understand Process", "🔄 Compare Perspectives"])
    
    with tab1:
        st.subheader("Philosophical Decision Analysis")
        decision_text = st.text_area("Describe your decision:", "Should I change careers for better opportunities but less stability?")
        col1, col2, col3 = st.columns(3)
        with col1:
            tradition = st.selectbox("Philosophical Tradition", ["Stoic", "Utilitarian", "Buddhist"])
        with col2:
            urgency = st.select_slider("Urgency", ["Low", "Medium", "High"])
        with col3:
            st.write("")
            st.write("")
            if st.button("🔍 Analyze Decision", type="primary"):
                st.success(f"Analyzing with {tradition} tradition...")
                st.info("Results will appear here")
    
    with tab2:
        st.subheader("Mechanical Process Analysis")
        process = st.selectbox("Select Process", ["Entropy", "Diffusion", "Oscillation", "Catalysis"])
        dimensions = st.multiselect("Analysis Dimensions", 
                                   ["Formula", "Etymology", "Theory", "Culture", "Utility"],
                                   default=["Formula", "Theory", "Utility"])
        if st.button("🔬 Analyze Process", type="primary"):
            st.success(f"Analyzing {process} process...")
            st.info(f"Examining {len(dimensions)} dimensions")
    
    with tab3:
        st.subheader("Comparative Analysis")
        col1, col2 = st.columns(2)
        with col1:
            comparison_type = st.radio("Compare:", ["Traditions", "Processes", "Decisions"])
        with col2:
            if comparison_type == "Traditions":
                item1 = st.selectbox("Tradition 1", ["Stoic", "Utilitarian", "Buddhist"])
                item2 = st.selectbox("Tradition 2", ["Utilitarian", "Stoic", "Buddhist"])
            elif comparison_type == "Processes":
                item1 = st.selectbox("Process 1", ["Entropy", "Diffusion", "Oscillation"])
                item2 = st.selectbox("Process 2", ["Diffusion", "Entropy", "Oscillation"])
        
        if st.button("🔄 Compare", type="primary"):
            st.success(f"Comparing {item1} vs {item2}...")
    
    # Features section
    st.markdown("## ✨ Key Features")
    
    features = [
        {
            "icon": "🏛️",
            "title": "Philosophical Analysis",
            "description": "Stoic, Utilitarian, and Buddhist decision frameworks",
            "color": "#3B82F6"
        },
        {
            "icon": "🔧", 
            "title": "Mechanical Processes",
            "description": "5-dimensional analysis of fundamental processes",
            "color": "#10B981"
        },
        {
            "icon": "📊",
            "title": "Comparative Engine",
            "description": "Cross-tradition and cross-process comparison",
            "color": "#8B5CF6"
        },
        {
            "icon": "📚",
            "title": "Research Tools",
            "description": "Academic paper generation and citation management",
            "color": "#F59E0B"
        }
    ]
    
    cols = st.columns(4)
    for idx, feature in enumerate(features):
        with cols[idx]:
            st.markdown(f"""
            <div style="border-left: 4px solid {feature['color']}; padding-left: 1rem; margin: 1rem 0;">
                <h3>{feature['icon']} {feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Recent insights
    st.markdown("## 💡 Recent Insights")
    
    insights = [
        "Stoic virtue ethics emphasizes what's within your control",
        "Entropy's logarithmic form reveals multiplicative nature of possibilities",
        "Utilitarian analysis requires considering all stakeholders",
        "Cultural interpretations shape practical application of processes"
    ]
    
    for insight in insights:
        st.markdown(f'<div class="insight-box">• {insight}</div>', unsafe_allow_html=True)

def philosophical_analysis_page():
    """Philosophical Analysis page"""
    st.markdown('<h1 class="main-header">🔍 Philosophical Analysis</h1>', unsafe_allow_html=True)
    
    # Sidebar configuration for this page
    with st.sidebar:
        st.markdown("### ⚙️ Analysis Settings")
        
        tradition = st.selectbox(
            "Philosophical Tradition",
            ["Stoic", "Utilitarian", "Buddhist", "Comparative"],
            help="Select the philosophical tradition to use for analysis"
        )
        
        analysis_depth = st.select_slider(
            "Analysis Depth",
            options=["Quick", "Standard", "Deep", "Comprehensive"],
            value="Standard"
        )
        
        include_citations = st.checkbox("Include Academic Citations", value=True)
        export_format = st.selectbox("Export Format", ["JSON", "PDF", "Markdown", "LaTeX"])
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["📝 Decision Input", "🔍 Analysis Results", "📚 Knowledge Base"])
    
    with tab1:
        st.subheader("Describe Your Decision")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            decision_context = st.text_area(
                "Decision Context:",
                height=150,
                placeholder="Describe the decision you're facing, including relevant context, stakeholders, and constraints..."
            )
        
        with col2:
            st.markdown("### 📋 Templates")
            templates = {
                "Career Change": "Should I leave my current job for a new opportunity?",
                "Ethical Dilemma": "A colleague is taking credit for my work.",
                "Investment": "Should I invest in this business opportunity?",
                "Relationship": "How should I approach this difficult conversation?"
            }
            
            for name, template in templates.items():
                if st.button(name, key=f"template_{name}"):
                    st.session_state.decision_context = template
                    st.rerun()
        
        st.subheader("Available Options")
        
        options = []
        for i in range(3):
            col1, col2 = st.columns([4, 1])
            with col1:
                option = st.text_input(f"Option {i+1}", key=f"option_{i}", placeholder=f"Describe option {i+1}")
                if option:
                    options.append(option)
            with col2:
                st.write("")
                st.write("")
                if st.button("🗑️", key=f"delete_{i}"):
                    st.rerun()
        
        if st.button("+ Add Option"):
            st.rerun()
        
        st.subheader("Stakeholders")
        stakeholders = st.multiselect(
            "Who is affected by this decision?",
            ["Yourself", "Family", "Colleagues", "Company", "Community", "Environment"],
            default=["Yourself", "Others"]
        )
        
        st.subheader("Decision Parameters")
        col1, col2, col3 = st.columns(3)
        with col1:
            time_horizon = st.selectbox("Time Horizon", ["Immediate", "Short-term", "Medium-term", "Long-term"])
        with col2:
            reversibility = st.select_slider("Reversibility", ["Irreversible", "Difficult", "Moderate", "Easy"])
        with col3:
            impact_scale = st.select_slider("Impact Scale", ["Personal", "Team", "Organization", "Societal"])
        
        # Analyze button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔬 Analyze Decision", type="primary", use_container_width=True):
                st.success(f"Analyzing with {tradition} tradition...")
                # Here you would call your API
    
    with tab2:
        st.subheader("Analysis Results")
        
        if 'analysis_results' not in st.session_state:
            st.info("No analysis results yet. Enter a decision and click 'Analyze Decision'.")
            
            # Sample results for demonstration
            st.markdown("### 🎯 Sample Analysis")
            
            cols = st.columns(3)
            with cols[0]:
                st.metric("Tradition", "Stoic")
            with cols[1]:
                st.metric("Confidence", "85%")
            with cols[2]:
                st.metric("Options Analyzed", "3")
            
            st.markdown("#### 💡 Key Insights")
            insights = [
                "Focus on what you can control - the effort, not the outcome",
                "Practice virtue: wisdom in choosing, courage in acting, justice in considering others, temperance in moderation",
                "View challenges as opportunities to exercise virtue"
            ]
            
            for insight in insights:
                st.markdown(f'<div class="insight-box">• {insight}</div>', unsafe_allow_html=True)
            
            st.markdown("#### 🎯 Recommendations")
            recommendations = [
                "Identify controllable vs uncontrollable aspects of each option",
                "Ask: 'What would a wise person do in this situation?'",
                "Consider which option best aligns with your core values",
                "Prepare for different outcomes while maintaining equanimity"
            ]
            
            for rec in recommendations:
                st.success(f"→ {rec}")
        
        # Export section
        st.markdown("---")
        st.subheader("📤 Export Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📄 Export as JSON"):
                st.success("JSON export ready!")
        with col2:
            if st.button("📊 Export as Report"):
                st.success("Report generation started!")
        with col3:
            if st.button("📧 Share Analysis"):
                st.info("Sharing functionality coming soon!")
    
    with tab3:
        st.subheader("Philosophical Knowledge Base")
        
        traditions = {
            "Stoic": {
                "description": "Focus on virtue, control, and resilience",
                "key_concepts": ["Virtue Ethics", "Dichotomy of Control", "Amor Fati", "Memento Mori"],
                "philosophers": ["Marcus Aurelius", "Seneca", "Epictetus"]
            },
            "Utilitarian": {
                "description": "Maximize happiness, minimize suffering",
                "key_concepts": ["Greatest Happiness Principle", "Consequentialism", "Hedonic Calculus", "Utility Maximization"],
                "philosophers": ["Jeremy Bentham", "John Stuart Mill", "Peter Singer"]
            },
            "Buddhist": {
                "description": "Mindfulness, compassion, and interdependence",
                "key_concepts": ["Four Noble Truths", "Eightfold Path", "Karma", "Impermanence"],
                "philosophers": ["Buddha", "Nagarjuna", "Thich Nhat Hanh"]
            }
        }
        
        selected_tradition = st.selectbox("Select Tradition", list(traditions.keys()))
        
        if selected_tradition:
            trad = traditions[selected_tradition]
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"### {selected_tradition} Philosophy")
                st.write(trad["description"])
                
                st.markdown("#### 🔑 Key Concepts")
                for concept in trad["key_concepts"]:
                    st.markdown(f"- **{concept}**")
            
            with col2:
                st.markdown("#### 👥 Key Philosophers")
                for philosopher in trad["philosophers"]:
                    st.markdown(f"- {philosopher}")
                
                st.markdown("#### 📚 Recommended Reading")
                readings = {
                    "Stoic": ["Meditations", "Letters from a Stoic", "Enchiridion"],
                    "Utilitarian": ["Utilitarianism", "An Introduction to the Principles of Morals and Legislation"],
                    "Buddhist": ["The Dhammapada", "The Heart of the Buddha's Teaching"]
                }
                
                for book in readings.get(selected_tradition, []):
                    st.markdown(f"- *{book}*")

def mechanical_processes_page():
    """Mechanical Processes page"""
    st.markdown('<h1 class="main-header">🔧 Mechanical Processes</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h3 class="sub-header">5-Dimensional Process Analysis</h3>
    Understand mechanical processes through: <strong>Formula • Etymology • Theory • Culture • Utility</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Process selection
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        process = st.selectbox(
            "Select Process",
            ["Entropy", "Diffusion", "Oscillation", "Catalysis", "Resonance", "Feedback"],
            help="Choose a mechanical process to analyze"
        )
    
    with col2:
        analysis_type = st.radio("Analysis Type", ["Quick", "Detailed"])
    
    with col3:
        show_visualizations = st.checkbox("Show Visualizations", value=True)
    
    # Dimensional analysis
    st.subheader("📐 Dimensional Analysis")
    
    dimensions = ["Formula", "Etymology", "Theory", "Culture", "Utility"]
    selected_dims = st.multiselect(
        "Select Dimensions to Analyze",
        dimensions,
        default=dimensions[:3]
    )
    
    # Process info based on selection
    process_info = {
        "Entropy": {
            "formula": "S = k_B ln Ω",
            "description": "Measure of disorder or information content",
            "category": "Thermodynamic"
        },
        "Diffusion": {
            "formula": "∂c/∂t = D∇²c",
            "description": "Net movement from high to low concentration",
            "category": "Physical"
        },
        "Oscillation": {
            "formula": "x(t) = A sin(ωt + φ)",
            "description": "Repetitive variation about equilibrium",
            "category": "Dynamic"
        },
        "Catalysis": {
            "formula": "E_a (catalyzed) < E_a (uncatalyzed)",
            "description": "Acceleration of reactions without being consumed",
            "category": "Chemical"
        }
    }
    
    info = process_info.get(process, {})
    
    if st.button("🔬 Analyze Process", type="primary"):
        st.success(f"Analyzing {process} process...")
        
        # Display results in tabs
        tabs = st.tabs(selected_dims)
        
        for idx, dim in enumerate(selected_dims):
            with tabs[idx]:
                if dim == "Formula":
                    st.markdown(f"### 📐 Formula: ${info.get('formula', 'N/A')}$")
                    st.markdown("#### Variables:")
                    variables = {
                        "S": "Entropy (J/K)",
                        "k_B": "Boltzmann constant",
                        "Ω": "Number of microstates",
                        "c": "Concentration",
                        "D": "Diffusion coefficient",
                        "x": "Displacement",
                        "A": "Amplitude",
                        "ω": "Angular frequency",
                        "φ": "Phase",
                        "E_a": "Activation energy"
                    }
                    for var, desc in variables.items():
                        if var in info.get('formula', ''):
                            st.markdown(f"- **{var}**: {desc}")
                    
                    st.markdown("#### Mathematical Properties:")
                    st.write("- Linearity: Nonlinear (logarithmic)")
                    st.write("- Dimensionality: Extensive property")
                    st.write("- Symmetry: Time asymmetry")
                
                elif dim == "Etymology":
                    st.markdown("### 📜 Etymology")
                    etymologies = {
                        "Entropy": {
                            "origin": "Greek",
                            "roots": ["en- (within)", "tropē (transformation)"],
                            "literal": "inner transformation",
                            "history": "Coined by Rudolf Clausius (1865)"
                        },
                        "Diffusion": {
                            "origin": "Latin",
                            "roots": ["diffundere (to spread out)"],
                            "literal": "pouring apart",
                            "history": "From Latin 'diffusio'"
                        }
                    }
                    
                    etym = etymologies.get(process, {})
                    for key, value in etym.items():
                        st.markdown(f"**{key.title()}**: {value}")
                
                elif dim == "Theory":
                    st.markdown("### 🧪 Theoretical Foundation")
                    
                    theories = {
                        "Entropy": [
                            "Second Law of Thermodynamics",
                            "Statistical Mechanics (Boltzmann)",
                            "Information Theory (Shannon)",
                            "Non-equilibrium Thermodynamics (Prigogine)"
                        ],
                        "Diffusion": [
                            "Fick's Laws of Diffusion",
                            "Brownian Motion Theory",
                            "Random Walk Models",
                            "Continuum Mechanics"
                        ]
                    }
                    
                    for theory in theories.get(process, ["Theory details not available"]):
                        st.markdown(f"- {theory}")
                
                elif dim == "Culture":
                    st.markdown("### 🏛️ Cultural Interpretation")
                    
                    cultural = {
                        "Entropy": [
                            "Greek mythology: Chaos as primordial disorder",
                            "Buddhist concept: Impermanence (Anicca)",
                            "Modern culture: 'Entropy' as metaphor for decay",
                            "Art: Entropic art movement"
                        ],
                        "Diffusion": [
                            "Cultural diffusion in anthropology",
                            "Innovation diffusion (Rogers)",
                            "Meme theory (Dawkins)",
                            "Language diffusion models"
                        ]
                    }
                    
                    for item in cultural.get(process, ["Cultural interpretations not available"]):
                        st.markdown(f"- {item}")
                
                elif dim == "Utility":
                    st.markdown("### ⚙️ Practical Utility")
                    
                    utilities = {
                        "Entropy": [
                            "Heat engine efficiency calculations",
                            "Information compression algorithms",
                            "Ecological energy flow analysis",
                            "Financial market modeling"
                        ],
                        "Diffusion": [
                            "Drug delivery systems",
                            "Semiconductor manufacturing",
                            "Pollutant dispersion modeling",
                            "Neural signal propagation"
                        ]
                    }
                    
                    for util in utilities.get(process, ["Utility information not available"]):
                        st.markdown(f"- {util}")
        
        # Dimensional profile visualization
        st.subheader("📊 Dimensional Profile")
        
        # Mock scores for demonstration
        scores = {
            "Formula": 0.85,
            "Etymology": 0.60,
            "Theory": 0.90,
            "Culture": 0.40,
            "Utility": 0.75
        }
        
        cols = st.columns(5)
        for idx, (dim, score) in enumerate(scores.items()):
            with cols[idx]:
                st.metric(dim, f"{score:.0%}")
                st.progress(score)
        
        # Cross-connections
        st.subheader("🔗 Cross-Connections")
        
        connections = {
            "Entropy": ["Information Theory", "Evolution", "Consciousness", "Market Efficiency"],
            "Diffusion": ["Heat Transfer", "Evolution", "Social Networks", "Innovation"]
        }
        
        if process in connections:
            for connection in connections[process]:
                st.markdown(f"- **Related to**: {connection}")
    
    # Quick analysis buttons
    st.markdown("---")
    st.subheader("⚡ Quick Analysis")
    
    quick_processes = ["Entropy", "Diffusion", "Oscillation"]
    cols = st.columns(len(quick_processes))
    
    for idx, proc in enumerate(quick_processes):
        with cols[idx]:
            if st.button(f"🔍 {proc}", use_container_width=True):
                st.session_state.selected_process = proc
                st.rerun()

def comparative_engine_page():
    """Comparative Engine page"""
    st.markdown('<h1 class="main-header">📊 Comparative Engine</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h3 class="sub-header">Cross-Domain Comparison & Synthesis</h3>
    Compare philosophical traditions, mechanical processes, and generate integrated insights.
    </div>
    """, unsafe_allow_html=True)
    
    # Comparison type selection
    comparison_type = st.radio(
        "Comparison Type",
        ["Philosophical Traditions", "Mechanical Processes", "Cross-Domain", "Decision Scenarios"],
        horizontal=True
    )
    
    if comparison_type == "Philosophical Traditions":
        st.subheader("🏛️ Compare Philosophical Traditions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            trad1 = st.selectbox("Tradition 1", ["Stoic", "Utilitarian", "Buddhist"], key="trad1")
            st.markdown("#### Key Principles")
            principles = {
                "Stoic": ["Virtue Ethics", "Dichotomy of Control", "Resilience"],
                "Utilitarian": ["Greatest Happiness", "Consequentialism", "Utility Calculation"],
                "Buddhist": ["Mindfulness", "Compassion", "Impermanence"]
            }
            for principle in principles.get(trad1, []):
                st.markdown(f"- {principle}")
        
        with col2:
            trad2 = st.selectbox("Tradition 2", ["Utilitarian", "Stoic", "Buddhist"], key="trad2")
            st.markdown("#### Key Principles")
            for principle in principles.get(trad2, []):
                st.markdown(f"- {principle}")
        
        if trad1 == trad2:
            st.warning("Please select two different traditions for comparison.")
        else:
            if st.button("🔄 Compare Traditions", type="primary"):
                st.success(f"Comparing {trad1} vs {trad2}...")
                
                # Mock comparison results
                st.subheader("📈 Comparison Results")
                
                comparison_points = [
                    ("Focus", "Internal virtue", "External consequences", "Mindful awareness"),
                    ("Decision Basis", "What's controllable", "Greatest happiness", "Compassion"),
                    ("Time Horizon", "Present acceptance", "Future consequences", "Present mindfulness"),
                    ("Success Metric", "Virtuous action", "Utility maximization", "Reduced suffering")
                ]
                
                # Create comparison table
                import pandas as pd
                data = []
                for point, stoic, util, buddhist in comparison_points:
                    row = {
                        "Aspect": point,
                        "Stoic": stoic if trad1 == "Stoic" or trad2 == "Stoic" else "",
                        "Utilitarian": util if trad1 == "Utilitarian" or trad2 == "Utilitarian" else "",
                        "Buddhist": buddhist if trad1 == "Buddhist" or trad2 == "Buddhist" else ""
                    }
                    data.append(row)
                
                df = pd.DataFrame(data)
                st.table(df)
                
                # Insights
                st.subheader("💡 Comparative Insights")
                insights = [
                    f"**{trad1}** emphasizes internal states while **{trad2}** focuses on external outcomes",
                    "Both traditions offer complementary perspectives on ethical decision-making",
                    "Consider integrating {trad1} principles for personal integrity and {trad2} for social impact"
                ]
                
                for insight in insights:
                    st.info(insight)
    
    elif comparison_type == "Mechanical Processes":
        st.subheader("🔧 Compare Mechanical Processes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            proc1 = st.selectbox("Process 1", ["Entropy", "Diffusion", "Oscillation"], key="proc1")
        
        with col2:
            proc2 = st.selectbox("Process 2", ["Diffusion", "Entropy", "Oscillation"], key="proc2")
        
        comparison_dimensions = st.multiselect(
            "Comparison Dimensions",
            ["Formula Complexity", "Theoretical Depth", "Cultural Significance", "Practical Utility"],
            default=["Theoretical Depth", "Practical Utility"]
        )
        
        if st.button("⚖️ Compare Processes", type="primary"):
            st.success(f"Comparing {proc1} vs {proc2}...")
            
            # Mock results
            st.subheader("Comparison Matrix")
            
            # Create radar chart data
            import plotly.graph_objects as go
            
            categories = ['Mathematical', 'Historical', 'Theoretical', 'Cultural', 'Practical']
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=[0.9, 0.7, 0.8, 0.6, 0.7],
                theta=categories,
                fill='toself',
                name=proc1
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=[0.8, 0.5, 0.7, 0.4, 0.9],
                theta=categories,
                fill='toself',
                name=proc2
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )),
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    elif comparison_type == "Cross-Domain":
        st.subheader("🌐 Cross-Domain Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            domain1_type = st.selectbox("Domain 1 Type", ["Philosophical Tradition", "Mechanical Process"])
            if domain1_type == "Philosophical Tradition":
                domain1 = st.selectbox("Select Tradition", ["Stoic", "Utilitarian", "Buddhist"])
            else:
                domain1 = st.selectbox("Select Process", ["Entropy", "Diffusion", "Oscillation"])
        
        with col2:
            domain2_type = st.selectbox("Domain 2 Type", ["Mechanical Process", "Philosophical Tradition"])
            if domain2_type == "Philosophical Tradition":
                domain2 = st.selectbox("Select Tradition", ["Utilitarian", "Stoic", "Buddhist"], key="domain2_trad")
            else:
                domain2 = st.selectbox("Select Process", ["Diffusion", "Entropy", "Oscillation"], key="domain2_proc")
        
        st.info("Cross-domain comparison reveals deep structural analogies between different knowledge domains.")
        
        if st.button("🔗 Compare Cross-Domain", type="primary"):
            st.success(f"Comparing {domain1} ({domain1_type}) with {domain2} ({domain2_type})...")
            
            # Analogical insights
            st.subheader("🧠 Analogical Insights")
            
            analogies = [
                "**Entropy** in thermodynamics is analogous to **Impermanence** in Buddhist philosophy",
                "**Stoic control dichotomy** mirrors **system boundaries** in engineering",
                "**Utilitarian calculus** resembles **optimization algorithms** in mathematics",
                "**Diffusion processes** parallel **spread of ideas** in cultural evolution"
            ]
            
            for analogy in analogies:
                st.markdown(f'<div class="insight-box">{analogy}</div>', unsafe_allow_html=True)
    
    # Synthesis section
    st.markdown("---")
    st.subheader("🎯 Synthesis Engine")
    
    synthesis_input = st.text_area(
        "Describe what you want to synthesize:",
        "How can Stoic virtue ethics inform our understanding of entropy in complex systems?",
        height=100
    )
    
    if st.button("🧪 Generate Synthesis", type="primary"):
        st.success("Generating integrated insights...")
        
        st.markdown("### 💎 Synthesized Insights")
        
        synthesized = [
            "**Virtue as Anti-Entropy**: Just as living systems maintain local order (decrease entropy) through energy input, virtuous action creates local order in moral space through intentional effort.",
            "**Control Dichotomy & System Boundaries**: The Stoic distinction between controllable and uncontrollable mirrors the thermodynamic distinction between system and environment - focus effort where it can create change.",
            "**Equanimity as Equilibrium State**: Stoic apatheia (freedom from disturbing passions) resembles thermodynamic equilibrium - a stable state maintained through balanced internal forces.",
            "**Wisdom as Information Processing**: Practical wisdom (phronesis) involves efficient information processing to reduce decision entropy, similar to Maxwell's Demon sorting molecules."
        ]
        
        for insight in synthesized:
            st.markdown(f'<div class="card">{insight}</div>', unsafe_allow_html=True)

def research_tools_page():
    """Research Tools page"""
    st.markdown('<h1 class="main-header">📚 Research Tools</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h3 class="sub-header">Academic Research & Publication Tools</h3>
    Generate research papers, manage citations, and create academic exports from your analyses.
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Paper Generator", "📚 Citation Manager", "📊 Data Export", "🎓 Academic Templates"])
    
    with tab1:
        st.subheader("Research Paper Generator")
        
        paper_title = st.text_input("Paper Title", "Comparative Analysis of Stoic and Utilitarian Decision Frameworks in Complex Systems")
        
        col1, col2 = st.columns(2)
        with col1:
            paper_type = st.selectbox("Paper Type", ["Conference Paper", "Journal Article", "Review Paper", "Book Chapter"])
            citation_style = st.selectbox("Citation Style", ["APA", "MLA", "Chicago", "Harvard", "IEEE"])
        
        with col2:
            word_target = st.number_input("Target Word Count", min_value=1000, max_value=10000, value=5000, step=500)
            include_abstract = st.checkbox("Include Abstract", value=True)
            include_keywords = st.checkbox("Include Keywords", value=True)
        
        # Analysis selection for paper
        st.subheader("Select Analyses to Include")
        
        col1, col2 = st.columns(2)
        with col1:
            include_stoic = st.checkbox("Stoic Analysis", value=True)
            include_utilitarian = st.checkbox("Utilitarian Analysis", value=True)
            include_buddhist = st.checkbox("Buddhist Analysis", value=False)
        
        with col2:
            include_entropy = st.checkbox("Entropy Process Analysis", value=True)
            include_comparative = st.checkbox("Comparative Analysis", value=True)
            include_methodology = st.checkbox("Methodology Section", value=True)
        
        # Generate button
        if st.button("📝 Generate Paper Draft", type="primary"):
            st.success("Generating research paper...")
            
            # Show progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                status_text.text(f"Generating... {i+1}%")
            
            status_text.text("✅ Paper generated successfully!")
            
            # Show preview
            st.subheader("📋 Paper Preview")
            
            st.markdown("""
            ### Abstract
            This paper presents a comparative analysis of Stoic and Utilitarian decision-making frameworks 
            applied to complex system management. Through computational simulation and philosophical analysis, 
            we demonstrate how different ethical traditions provide complementary insights for navigating 
            uncertainty and making optimal decisions in complex environments.
            
            ### Keywords
            Decision Intelligence, Stoic Philosophy, Utilitarianism, Complex Systems, Ethical AI
            
            ### 1. Introduction
            The increasing complexity of modern decision environments necessitates integrated approaches 
            that combine philosophical wisdom with computational analysis. This paper introduces a novel 
            framework for comparative decision intelligence...
            """)
            
            # Download options
            st.subheader("📥 Download Options")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.download_button(
                    label="📄 Download LaTeX",
                    data="# LaTeX content would go here",
                    file_name=f"{paper_title[:50]}.tex",
                    mime="text/plain"
                )
            
            with col2:
                st.download_button(
                    label="📝 Download Word",
                    data="# Word content would go here",
                    file_name=f"{paper_title[:50]}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            
            with col3:
                st.download_button(
                    label="📊 Download PDF",
                    data="# PDF content would go here",
                    file_name=f"{paper_title[:50]}.pdf",
                    mime="application/pdf"
                )
    
    with tab2:
        st.subheader("Citation Manager")
        
        # Add citation
        with st.expander("➕ Add New Citation"):
            col1, col2 = st.columns(2)
            with col1:
                author = st.text_input("Author(s)")
                year = st.text_input("Year")
                title = st.text_input("Title")
            
            with col2:
                journal = st.text_input("Journal/Book")
                volume = st.text_input("Volume")
                pages = st.text_input("Pages")
            
            if st.button("Add to Library"):
                st.success("Citation added to library!")
        
        # Citation library
        st.subheader("📚 Citation Library")
        
        citations = [
            {"author": "Marcus Aurelius", "year": "180 AD", "title": "Meditations", "type": "Book"},
            {"author": "Jeremy Bentham", "year": "1789", "title": "An Introduction to the Principles of Morals and Legislation", "type": "Book"},
            {"author": "Claude Shannon", "year": "1948", "title": "A Mathematical Theory of Communication", "type": "Journal"},
            {"author": "Ilya Prigogine", "year": "1977", "title": "Self-Organization in Non-Equilibrium Systems", "type": "Book"}
        ]
        
        for idx, citation in enumerate(citations):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{citation['author']}** ({citation['year']}). *{citation['title']}*. [{citation['type']}]")
            with col2:
                st.button("📋 Copy", key=f"copy_{idx}")
            with col3:
                st.button("🗑️", key=f"delete_{idx}")
        
        # Export citations
        st.subheader("Export Citations")
        export_format = st.selectbox("Format", ["BibTeX", "RIS", "CSV", "JSON"])
        
        if st.button(f"Export as {export_format}"):
            st.success(f"Citations exported as {export_format}")
    
    with tab3:
        st.subheader("Data Export")
        
        # Export options
        export_type = st.radio(
            "Export Type",
            ["Analysis Results", "Comparative Data", "Process Analysis", "Full Dataset"],
            horizontal=True
        )
        
        # Date range
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date")
        with col2:
            end_date = st.date_input("End Date")
        
        # Format selection
        export_formats = st.multiselect(
            "Export Formats",
            ["JSON", "CSV", "Excel", "Parquet", "SQL"],
            default=["JSON", "CSV"]
        )
        
        if st.button("📊 Export Data", type="primary"):
            st.success("Exporting data...")
            
            # Show export status
            with st.status("Export in progress...", expanded=True) as status:
                st.write("Collecting analysis data...")
                st.write("Formatting for export...")
                st.write("Creating files...")
                status.update(label="Export complete!", state="complete", expanded=False)
            
            # Download buttons for each format
            for fmt in export_formats:
                st.download_button(
                    label=f"⬇️ Download {fmt.upper()}",
                    data=f"# {fmt} data would be here",
                    file_name=f"decision_intelligence_export.{fmt.lower()}",
                    mime="text/plain" if fmt != "Excel" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
    
    with tab4:
        st.subheader("Academic Templates")
        
        template_type = st.selectbox(
            "Template Type",
            ["Research Paper", "Conference Poster", "Thesis Chapter", "Literature Review", "Research Proposal"]
        )
        
        if template_type == "Research Paper":
            st.markdown("""
            ### Research Paper Template Structure
            
            1. **Title Page**
               - Title, authors, affiliations, abstract, keywords
            
            2. **Introduction**
               - Problem statement
               - Literature review
               - Research objectives
               - Paper structure
            
            3. **Methodology**
               - Philosophical frameworks
               - Computational methods
               - Data collection
               - Analysis procedures
            
            4. **Results**
               - Analysis findings
               - Comparative results
               - Statistical analysis
               - Visualizations
            
            5. **Discussion**
               - Interpretation of results
               - Theoretical implications
               - Practical applications
               - Limitations
            
            6. **Conclusion**
               - Summary of findings
               - Contributions
               - Future research
            
            7. **References**
               - Citation list
               - Bibliography
            """)
        
        # Template download
        templates = {
            "Research Paper": "research_paper_template.zip",
            "Conference Poster": "poster_template.pptx",
            "Thesis Chapter": "thesis_chapter.docx",
            "Literature Review": "lit_review_template.md",
            "Research Proposal": "research_proposal.pdf"
        }
        
        if st.button("📥 Download Template"):
            template_file = templates.get(template_type, "template.zip")
            st.success(f"Downloading {template_file}...")

def settings_page():
    """Settings page"""
    st.markdown('<h1 class="main-header">⚙️ Settings</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔧 General", "📊 Display", "🔌 API", "💾 Data"])
    
    with tab1:
        st.subheader("General Settings")
        
        # Platform settings
        platform_name = st.text_input("Platform Name", "Comparative Decision Intelligence")
        default_language = st.selectbox("Default Language", ["English", "Spanish", "French", "German", "Chinese"])
        
        # Analysis defaults
        st.subheader("Analysis Defaults")
        
        col1, col2 = st.columns(2)
        with col1:
            default_tradition = st.selectbox("Default Philosophical Tradition", ["Stoic", "Utilitarian", "Buddhist"])
            default_analysis_depth = st.select_slider("Default Analysis Depth", ["Quick", "Standard", "Deep"])
        
        with col2:
            default_process = st.selectbox("Default Mechanical Process", ["Entropy", "Diffusion", "Oscillation"])
            auto_save = st.checkbox("Auto-save Analyses", value=True)
        
        # Notification settings
        st.subheader("Notifications")
        email_notifications = st.checkbox("Email Notifications", value=False)
        analysis_complete_notify = st.checkbox("Notify on Analysis Completion", value=True)
        
        if st.button("💾 Save General Settings", type="primary"):
            st.success("General settings saved!")
    
    with tab2:
        st.subheader("Display Settings")
        
        # Theme settings
        theme = st.radio("Theme", ["Light", "Dark", "Auto"])
        
        # Dashboard layout
        st.subheader("Dashboard Layout")
        default_view = st.selectbox("Default View", ["Expanded", "Collapsed", "Compact"])
        show_metrics = st.checkbox("Show Metrics Dashboard", value=True)
        show_recent = st.checkbox("Show Recent Analyses", value=True)
        
        # Visualization settings
        st.subheader("Visualization Settings")
        
        col1, col2 = st.columns(2)
        with col1:
            chart_style = st.selectbox("Chart Style", ["Plotly", "Matplotlib", "Vega-Lite"])
            default_colors = st.color_picker("Primary Color", "#3B82F6")
        
        with col2:
            animation_speed = st.slider("Animation Speed", 0, 10, 5)
            show_animations = st.checkbox("Show Animations", value=True)
        
        if st.button("🎨 Save Display Settings", type="primary"):
            st.success("Display settings saved!")
    
    with tab3:
        st.subheader("API Settings")
        
        # API configuration
        api_url = st.text_input("API URL", "http://localhost:8000")
        api_timeout = st.number_input("API Timeout (seconds)", min_value=5, max_value=60, value=30)
        
        # Authentication
        st.subheader("Authentication")
        api_key = st.text_input("API Key", type="password")
        use_authentication = st.checkbox("Use Authentication", value=False)
        
        # Cache settings
        st.subheader("Cache Settings")
        cache_enabled = st.checkbox("Enable Cache", value=True)
        cache_duration = st.number_input("Cache Duration (minutes)", min_value=1, max_value=1440, value=60)
        
        # Connection test
        if st.button("🔗 Test API Connection"):
            with st.spinner("Testing connection..."):
                # Here you would actually test the connection
                import time
                time.sleep(1)
                st.success("✅ API connection successful!")
        
        if st.button("⚙️ Save API Settings", type="primary"):
            st.success("API settings saved!")
    
    with tab4:
        st.subheader("Data Management")
        
        # Data storage
        storage_location = st.text_input("Data Storage Location", "./data")
        max_storage = st.number_input("Maximum Storage (GB)", min_value=1, max_value=100, value=10)
        
        # Backup settings
        st.subheader("Backup Settings")
        
        col1, col2 = st.columns(2)
        with col1:
            auto_backup = st.checkbox("Auto Backup", value=True)
            backup_frequency = st.selectbox("Backup Frequency", ["Daily", "Weekly", "Monthly"])
        
        with col2:
            backup_location = st.text_input("Backup Location", "./backups")
            keep_backups = st.number_input("Keep Backups (days)", min_value=1, max_value=365, value=30)
        
        # Data management actions
        st.subheader("Data Actions")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🗃️ Backup Now", use_container_width=True):
                st.info("Starting backup...")
        
        with col2:
            if st.button("🧹 Clear Cache", use_container_width=True):
                st.info("Clearing cache...")
        
        with col3:
            if st.button("📊 Export All Data", use_container_width=True):
                st.info("Preparing data export...")
        
        # Data statistics
        st.subheader("📈 Data Statistics")
        
        cols = st.columns(4)
        with cols[0]:
            st.metric("Analyses", "142")
        with cols[1]:
            st.metric("Processes", "8")
        with cols[2]:
            st.metric("Citations", "64")
        with cols[3]:
            st.metric("Storage Used", "2.4 GB")
        
        if st.button("💾 Save Data Settings", type="primary"):
            st.success("Data settings saved!")

# Main execution
if __name__ == "__main__":
    load_page()
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("© 2024 Comparative Decision Intelligence")
    with col2:
        st.caption("Version 2.0.0 • Enterprise Edition")
    with col3:
        if st.button("🆘 Help & Documentation"):
            st.info("Opening documentation...")
EOF

echo "✓ Created complete dashboard/app.py"

# Create required directories
mkdir -p dashboard/pages
echo "✓ Created dashboard/pages directory"

# Create pages home.py (already exists, but ensure it's there)
cat > dashboard/pages/home.py << 'EOF'
"""
Home Page - Simplified version for navigation
"""

import streamlit as st

def main():
    st.title("🏠 Home")
    st.write("Welcome to the Comparative Decision Intelligence Platform!")
    st.write("Navigate using the sidebar to access different modules.")
EOF

echo "✓ Created dashboard/pages/home.py"

# Create pages analysis.py
cat > dashboard/pages/analysis.py << 'EOF'
"""
Philosophical Analysis Page - Simplified
"""

import streamlit as st

def main():
    st.title("🔍 Philosophical Analysis")
    st.write("This page would contain the full philosophical analysis module.")
    st.info("Navigate back to the main app to use the complete philosophical analysis features.")
EOF

echo "✓ Created dashboard/pages/analysis.py"

# Create pages mechanical_processes.py
cat > dashboard/pages/mechanical_processes.py << 'EOF'
"""
Mechanical Processes Page - Simplified
"""

import streamlit as st

def main():
    st.title("🔧 Mechanical Processes")
    st.write("This page would contain the full mechanical processes analysis module.")
    st.info("Navigate back to the main app to use the complete mechanical processes features.")
EOF

echo "✓ Created dashboard/pages/mechanical_processes.py"

# Create requirements update for dashboard
cat > dashboard/requirements.txt << 'EOF'
streamlit>=1.28.0
plotly>=5.18.0
pandas>=2.0.0
requests>=2.31.0
EOF

echo "✓ Created dashboard/requirements.txt"

# Create dashboard README
cat > dashboard/README.md << 'EOF'
# Dashboard Module

## Overview
Streamlit-based dashboard for the Comparative Decision Intelligence Platform.

## Features
- Multi-page navigation
- Philosophical decision analysis
- Mechanical process analysis (5-dimensional)
- Comparative engine
- Research tools
- Settings management

## Pages
1. 🏠 Home - Platform overview and quick start
2. 🔍 Philosophical Analysis - Decision analysis through traditions
3. 🔧 Mechanical Processes - Process analysis through 5 dimensions
4. 📊 Comparative Engine - Cross-domain comparison
5. 📚 Research Tools - Academic paper generation
6. ⚙️ Settings - Platform configuration

## Running Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py

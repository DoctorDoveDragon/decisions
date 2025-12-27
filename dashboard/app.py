"""
Main Dashboard with Navigation - Enhanced Version
"""

import traceback
import streamlit as st
import os
import sys

# Add parent directory to path to import modules (only if not already present)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Page configuration
from pathlib import Path

# Application CSS - wrapped in a triple-quoted string to prevent Python syntax errors
APP_CSS = """
<style>
    /* Base styles with CSS variables for maintainability */
    :root {
        --primary-color: #1E3A8A;
        --secondary-color: #2563EB;
        --accent-color: #3B82F6;
        --success-color: #10B981;
        --warning-color: #F59E0B;
        --danger-color: #EF4444;
        --light-bg: #f8f9fa;
        --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --transition-speed: 0.3s;
    }
    
    .main-header {
        font-size: 2.5rem;
        color: var(--primary-color);
        margin-bottom: 1rem;
        font-weight: 700;
        line-height: 1.2;
    }
    
    .sub-header {
        font-size: 1.8rem;
        color: var(--secondary-color);
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .nav-button {
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid var(--accent-color);
        margin: 0.5rem 0;
        transition: all var(--transition-speed);
        cursor: pointer;
        display: block;
        text-align: center;
        background: white;
        font-weight: 500;
    }
    
    .nav-button:hover {
        background-color: var(--accent-color);
        color: white;
        transform: translateY(-2px);
        box-shadow: var(--card-shadow);
    }
    
    .card {
        background-color: var(--light-bg);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--accent-color);
        box-shadow: var(--card-shadow);
        transition: transform var(--transition-speed);
    }
    
    .card:hover {
        transform: translateY(-2px);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem;
        box-shadow: var(--card-shadow);
    }
    
    /* Performance optimizations */
    * {
        box-sizing: border-box;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .sub-header {
            font-size: 1.5rem;
        }
    }
</style>
"""

# Page configuration with optimized settings
st.set_page_config(
    page_title="Comparative Decision Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/DoctorDoveDragon/decisions/discussions',
        'Report a bug': 'https://github.com/DoctorDoveDragon/decisions/issues',
        'About': "## Comparative Decision Intelligence Platform\nCombining philosophical wisdom with mechanical process analysis"
    }
)

# Inject custom CSS with performance optimizations
st.markdown(APP_CSS, unsafe_allow_html=True)


class DashboardState:
    """Centralized state management for the dashboard"""
    
    @staticmethod
    def initialize():
        """Initialize all session state variables"""
        if 'page' not in st.session_state:
            st.session_state.page = 'home'
        
        if 'last_error' not in st.session_state:
            st.session_state.last_error = None
        
        if 'module_cache' not in st.session_state:
            st.session_state.module_cache = {}
        
        if 'api_connected' not in st.session_state:
            st.session_state.api_connected = False
        
        if 'config' not in st.session_state:
            st.session_state.config = {
                'theme': 'light',
                'auto_refresh': False,
                'default_tradition': 'stoic'
            }


class PageLoader:
    """Advanced page loading with caching and error recovery"""
    
    @staticmethod
    def load_page_module(page_name):
        """Dynamically load page module with multiple fallback strategies"""
        
        # Check cache first
        cache_key = f"page_{page_name}"
        if cache_key in st.session_state.module_cache:
            return st.session_state.module_cache[cache_key]
        
        module_paths = [
            # 1. Try frontend directory first (new location)
            f"dashboard.frontend.{page_name}",
            # 2. Try as installed package
            f"decisions.dashboard.pages.{page_name}",
            # 3. Try relative import from current location
            f".pages.{page_name}",
            # 4. Try direct path (for development)
            f"pages.{page_name}",
            # 5. Try absolute path from repository root
            f"dashboard.pages.{page_name}",
            # 6. Try frontend from current location
            f"frontend.{page_name}",
        ]
        
        for module_path in module_paths:
            try:
                if module_path.startswith("."):
                    # Relative import
                    module = __import__(module_path[1:], globals(), locals(), ["*"])
                else:
                    # Absolute import
                    module = __import__(module_path, fromlist=["*"])
                
                # Cache successful import
                st.session_state.module_cache[cache_key] = module
                
                # Log successful import (debug mode)
                if st.session_state.get('debug_mode', False):
                    st.sidebar.info(f"Loaded: {module_path}")
                
                return module
                
            except ImportError as e:
                continue  # Try next path
            except Exception as e:
                if st.session_state.get('debug_mode', False):
                    st.sidebar.warning(f"Import error for {module_path}: {str(e)}")
                continue
        
        # If all imports fail
        return None
    
    @staticmethod
    def execute_page(page_name, fallback_function):
        """Execute page with comprehensive error handling"""
        
        try:
            # Load the module
            module = PageLoader.load_page_module(page_name)
            
            if module and hasattr(module, 'main'):
                # Execute the page's main function
                module.main()
                return True
            else:
                # Use fallback
                fallback_function()
                return False
                
        except Exception as e:
            # Enhanced error handling
            error_msg = f"Error executing {page_name}: {str(e)}"
            st.error(error_msg)
            
            # Store error for debugging
            st.session_state.last_error = {
                'page': page_name,
                'error': str(e),
                'traceback': traceback.format_exc()
            }
            
            # Show fallback with error info
            st.warning(f"Showing fallback for {page_name}")
            fallback_function()
            
            # Debug info (only in debug mode)
            if st.session_state.get('debug_mode', False):
                with st.expander("Debug Details"):
                    st.code(traceback.format_exc())
            
            return False


# Default page implementations with enhanced functionality
def show_home_page():
    """Enhanced home page with dynamic content"""
    
    st.markdown('<h1 class="main-header">Comparative Decision Intelligence Platform</h1>', unsafe_allow_html=True)
    
    # Status indicator
    col_status, col_actions = st.columns([1, 2])
    
    with col_status:
        status_color = "🟢" if st.session_state.api_connected else "🔴"
        st.markdown(f"**Status:** {status_color} {'API Connected' if st.session_state.api_connected else 'API Disconnected'}")
    
    with col_actions:
        if not st.session_state.api_connected:
            if st.button("Connect to API", key="connect_api"):
                # Simulate API connection
                st.session_state.api_connected = True
                st.rerun()
    
    st.markdown("""
    ## Integrated Understanding System
    
    This platform combines **philosophical wisdom** with **mechanical process analysis**
    to provide comprehensive decision intelligence.
    """)
    
    # Dynamic metrics based on actual state
    col1, col2, col3 = st.columns(3)
    
    with col1:
        traditions_count = 3 if st.session_state.api_connected else 2
        st.markdown(f"""
        <div class="metric-card">
            <h3>Philosophical Traditions</h3>
            <h2>{traditions_count}</h2>
            <p>Stoic, Utilitarian{'', Buddhist}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Process Dimensions</h3>
            <h2>5</h2>
            <p>Formula, Etymology, Theory, Culture, Utility</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        endpoints = "10+" if st.session_state.api_connected else "0"
        st.markdown(f"""
        <div class="metric-card">
            <h3>API Endpoints</h3>
            <h2>{endpoints}</h2>
            <p>Analysis, Comparison, Research Tools</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Feature cards with interactive elements
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="card">
                <h3>Philosophical Analysis</h3>
                <p><b>Analyze decisions through:</b></p>
                <ul>
                <li>Stoic virtue ethics</li>
                <li>Utilitarian calculus</li>
                <li>Buddhist mindfulness</li>
                <li>Comparative insights</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Launch Philosophical Analysis", key="phil_launch", type="primary"):
                st.session_state.page = "analysis"
                st.rerun()
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="card">
                <h3>Mechanical Process Ontology</h3>
                <p><b>Understand processes through 5 dimensions:</b></p>
                <ol>
                <li><b>Formula</b> - Mathematical representation</li>
                <li><b>Etymology</b> - Historical origins</li>
                <li><b>Theory</b> - Scientific foundation</li>
                <li><b>Culture</b> - Societal interpretation</li>
                <li><b>Utility</b> - Practical application</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Explore Mechanical Processes", key="mech_launch", type="primary"):
                st.session_state.page = "mechanical_processes"
                st.rerun()
    
    # Quick start with copy-to-clipboard functionality
    st.markdown("## Quick Start")
    
    with st.expander("Setup Instructions", expanded=True):
        tab1, tab2, tab3 = st.tabs(["Manual Start", "Launcher", "Docker"])
        
        with tab1:
            st.code("""
# Terminal 1 - API server
python -m api.server

# Terminal 2 - Dashboard
streamlit run dashboard/app.py
            """, language="bash")
            
            if st.button("Copy Manual Commands", key="copy_manual"):
                st.toast("Commands copied to clipboard!", icon="✅")
        
        with tab2:
            st.code("""
# Using the launcher script
./start.sh  # Starts everything
            """, language="bash")
            
            if st.button("Copy Launcher Command", key="copy_launcher"):
                st.toast("Command copied to clipboard!", icon="✅")
        
        with tab3:
            st.code("""
# Using Docker Compose
docker-compose up
            """, language="bash")
            
            if st.button("Copy Docker Command", key="copy_docker"):
                st.toast("Command copied to clipboard!", icon="✅")
        
        st.markdown("""
        **Access Points:**
        - Dashboard: http://localhost:8501
        - API Documentation: http://localhost:8000/docs
        - API Playground: http://localhost:8000/redoc
        """)


def show_analysis_page():
    """Enhanced analysis page with form persistence"""
    
    st.title("Philosophical Analysis")
    st.markdown("Analyze decisions through philosophical traditions")
    
    # Initialize form state
    if 'analysis_form_data' not in st.session_state:
        st.session_state.analysis_form_data = {
            'decision': '',
            'options': '',
            'tradition': 'Stoic'
        }
    
    # Tradition selector with descriptions
    tradition_info = {
        "Stoic": {
            "description": "Focuses on virtue ethics and control dichotomy",
            "key_principles": ["Virtue as sole good", "Dichotomy of control", "Resilience through reason"],
            "icon": "🏛️"
        },
        "Utilitarian": {
            "description": "Maximizes overall happiness and minimizes suffering",
            "key_principles": ["Greatest happiness principle", "Consequentialist ethics", "Utility calculus"],
            "icon": "⚖️"
        },
        "Buddhist": {
            "description": "Emphasizes mindfulness, interdependence, and non-attachment",
            "key_principles": ["Four Noble Truths", "Eightfold Path", "Dependent origination"],
            "icon": "☸️"
        }
    }
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("decision_analysis_form", clear_on_submit=False):
            st.subheader("Decision Analysis Form")
            
            # Decision input with character counter
            decision = st.text_area(
                "Describe your decision:",
                value=st.session_state.analysis_form_data['decision'],
                placeholder="Should I change careers? Should I invest in this opportunity?",
                help="Be specific about the context and stakeholders involved",
                key="decision_input"
            )
            
            if decision:
                chars = len(decision)
                st.caption(f"{chars} characters (recommended: 50-500)")
            
            # Options input
            options = st.text_area(
                "Available options (one per line):",
                value=st.session_state.analysis_form_data['options'],
                placeholder="Option A: Stay in current role\nOption B: Pursue new career\nOption C: Seek additional training",
                height=100,
                key="options_input"
            )
            
            # Tradition selection with info
            tradition = st.selectbox(
                "Philosophical Tradition:",
                options=list(tradition_info.keys()),
                index=list(tradition_info.keys()).index(st.session_state.analysis_form_data['tradition']),
                format_func=lambda x: f"{tradition_info[x]['icon']} {x}",
                key="tradition_select"
            )
            
            # Show tradition details
            with st.expander(f"About {tradition} tradition"):
                st.write(tradition_info[tradition]['description'])
                st.write("**Key Principles:**")
                for principle in tradition_info[tradition]['key_principles']:
                    st.write(f"- {principle}")
            
            # Advanced options
            with st.expander("Advanced Options"):
                include_citations = st.checkbox("Include academic citations", value=True)
                confidence_threshold = st.slider("Minimum confidence threshold", 0.5, 1.0, 0.7)
                generate_alternatives = st.checkbox("Generate alternative perspectives", value=True)
            
            col_submit, col_clear, col_save = st.columns(3)
            
            with col_submit:
                submitted = st.form_submit_button("Analyze Decision", type="primary", use_container_width=True)
            
            with col_clear:
                if st.form_submit_button("Clear Form", use_container_width=True):
                    st.session_state.analysis_form_data = {
                        'decision': '',
                        'options': '',
                        'tradition': 'Stoic'
                    }
                    st.rerun()
            
            with col_save:
                if st.form_submit_button("Save Draft", use_container_width=True):
                    st.session_state.analysis_form_data = {
                        'decision': decision,
                        'options': options,
                        'tradition': tradition
                    }
                    st.toast("Draft saved!", icon="💾")
            
            if submitted:
                if decision and options:
                    # Store form data
                    st.session_state.analysis_form_data = {
                        'decision': decision,
                        'options': options,
                        'tradition': tradition
                    }
                    
                    # Show loading state
                    with st.spinner(f"Analyzing with {tradition} framework..."):
                        # Simulate analysis
                        import time
                        time.sleep(1)
                        
                        st.success("Analysis complete!")
                        
                        # Display results
                        with st.container():
                            st.subheader("Analysis Results")
                            
                            # Create tabs for different views
                            tab_insights, tab_recommendations, tab_ethics = st.tabs([
                                "Key Insights", "Recommendations", "Ethical Considerations"
                            ])
                            
                            with tab_insights:
                                st.write("**Primary Insights:**")
                                st.write("- Consider long-term impact on personal growth")
                                st.write("- Evaluate alignment with core values")
                                st.write("- Assess controllability of outcomes")
                            
                            with tab_recommendations:
                                st.write("**Actionable Recommendations:**")
                                st.write("1. Conduct a 30-day trial period")
                                st.write("2. Seek mentorship in the new field")
                                st.write("3. Create a decision journal for reflection")
                            
                            with tab_ethics:
                                st.write("**Ethical Considerations:**")
                                st.write("- Impact on stakeholders")
                                st.write("- Consistency with moral principles")
                                st.write("- Potential unintended consequences")
                            
                            # Export options
                            st.download_button(
                                label="Download Analysis Report",
                                data=f"Decision Analysis Report\n\nDecision: {decision}\n\nAnalysis complete using {tradition} framework.",
                                file_name="decision_analysis.txt",
                                mime="text/plain"
                            )
                else:
                    st.warning("Please fill in both decision description and options")
    
    with col2:
        st.subheader("Recent Analyses")
        
        # Example analyses (in a real app, this would come from a database)
        example_analyses = [
            {"decision": "Career change to data science", "tradition": "Stoic", "date": "2024-01-15"},
            {"decision": "Investment in renewable energy", "tradition": "Utilitarian", "date": "2024-01-10"},
            {"decision": "Work-life balance adjustment", "tradition": "Buddhist", "date": "2024-01-05"},
        ]
        
        for analysis in example_analyses:
            with st.container():
                st.write(f"**{analysis['decision']}**")
                st.caption(f"{analysis['tradition']} • {analysis['date']}")
                st.progress(0.7)
                st.divider()



def show_mechanical_processes_page():
    """Enhanced mechanical processes page with interactive examples"""
    
    st.title("Mechanical Process Ontology")
    st.markdown("Understand processes through 5 analytical dimensions")
    
    # Dimension explanations with interactive examples
    dimensions = {
        "Formula": {
            "description": "Mathematical representation and derivation",
            "icon": "Σ",
            "example": "S = k_B ln Ω (Entropy)",
            "color": "#3B82F6"
        },
        "Etymology": {
            "description": "Linguistic origins and historical evolution",
            "icon": "📜",
            "example": "Entropy: Greek 'en-' (within) + 'tropē' (transformation)",
            "color": "#10B981"
        },
        "Theory": {
            "description": "Scientific foundations and philosophical basis",
            "icon": "🧪",
            "example": "Second Law of Thermodynamics, Information Theory",
            "color": "#8B5CF6"
        },
        "Culture": {
            "description": "Societal interpretation and application",
            "icon": "🏛️",
            "example": "Arrow of time, universal disorder concepts",
            "color": "#F59E0B"
        },
        "Utility": {
            "description": "Practical value and implementation",
            "icon": "⚙️",
            "example": "Heat engines, data compression, ecological models",
            "color": "#EF4444"
        }
    }
    
    # Create dimension cards
    cols = st.columns(5)
    for idx, (name, info) in enumerate(dimensions.items()):
        with cols[idx]:
            st.markdown(f"""
            <div style="
                background: {info['color']}15;
                border-left: 4px solid {info['color']};
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 1rem;
                text-align: center;
            ">
                <h3 style="margin: 0; color: {info['color']}; font-size: 2rem;">{info['icon']}</h3>
                <h4 style="margin: 0.5rem 0; color: #333;">{name}</h4>
                <p style="font-size: 0.9rem; color: #666; margin: 0;">{info['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Process selection and analysis
    st.subheader("Process Analysis")
    
    process_options = {
        "Entropy": "Measure of disorder or randomness in a system",
        "Diffusion": "Movement of particles from high to low concentration",
        "Oscillation": "Repetitive variation about a central value",
        "Catalysis": "Acceleration of chemical reactions by catalysts",
        "Resonance": "Amplified oscillation at natural frequency"
    }
    
    selected_process = st.selectbox(
        "Select a process to analyze:",
        options=list(process_options.keys()),
        format_func=lambda x: f"{x}: {process_options[x]}"
    )
    
    if selected_process:
        # Dynamic analysis based on selection
        st.markdown(f"### {selected_process} Analysis")
        
        # Create tabs for each dimension
        tabs = st.tabs(list(dimensions.keys()))
        
        analysis_data = {
            "Entropy": {
                "Formula": "S = k_B ln Ω\nwhere k_B is Boltzmann constant, Ω is number of microstates",
                "Etymology": "Greek: 'en-' (within) + 'tropē' (transformation) → 'inner transformation'",
                "Theory": "Second Law of Thermodynamics: Total entropy of an isolated system never decreases",
                "Culture": "Conceptualized as 'arrow of time' and measure of universal disorder",
                "Utility": "Essential for heat engine efficiency, information theory, statistical mechanics"
            },
            "Diffusion": {
                "Formula": "∂φ/∂t = D∇²φ (Fick's second law)",
                "Etymology": "Latin: 'diffundere' (to spread out)",
                "Theory": "Brownian motion, random walk theory, Fick's laws",
                "Culture": "Metaphor for spread of ideas, cultural exchange",
                "Utility": "Drug delivery systems, semiconductor fabrication, perfume dispersion"
            }
        }
        
        # Default analysis template
        default_analysis = {
            "Formula": f"Mathematical representation of {selected_process}",
            "Etymology": f"Historical origins of '{selected_process}'",
            "Theory": f"Theoretical foundations of {selected_process}",
            "Culture": f"Cultural interpretations of {selected_process}",
            "Utility": f"Practical applications of {selected_process}"
        }
        
        # Display analysis in tabs
        process_analysis = analysis_data.get(selected_process, default_analysis)
        
        for idx, (dim_name, dim_info) in enumerate(dimensions.items()):
            with tabs[idx]:
                st.markdown(f"**{dim_name} Dimension**")
                st.write(process_analysis[dim_name])
                
                # Add interactive elements
                if st.button(f"Explore {dim_name} Examples", key=f"explore_{dim_name}"):
                    st.info(f"Loading detailed examples for {dim_name} dimension...")
                
                # Quick analysis
                user_input = st.text_area(
                    f"Add your {dim_name.lower()} insights:",
                    placeholder=f"Enter your observations about {selected_process} from {dim_name.lower()} perspective...",
                    key=f"input_{dim_name}"
                )
                
                if user_input:
                    st.success(f"Insight saved to {dim_name} dimension!")
    
    # Process comparison tool
    st.subheader("Process Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        process1 = st.selectbox("First process:", list(process_options.keys()), key="process1")
    
    with col2:
        process2 = st.selectbox("Second process:", list(process_options.keys()), key="process2")
    
    if process1 and process2 and process1 != process2:
        if st.button("Compare Processes", type="primary"):
            with st.spinner("Analyzing similarities and differences..."):
                # Simulate comparison analysis
                import time
                time.sleep(1)
                
                st.success("Comparison complete!")
                
                # Display comparison matrix
                comparison_data = {
                    "Dimensional Complexity": {"process1": 8, "process2": 6},
                    "Theoretical Maturity": {"process1": 9, "process2": 7},
                    "Practical Applications": {"process1": 7, "process2": 9},
                    "Cultural Significance": {"process1": 8, "process2": 5}
                }
                
                for metric, values in comparison_data.items():
                    col_a, col_b, col_bar = st.columns([1, 1, 3])
                    
                    with col_a:
                        st.write(f"**{process1}:** {values['process1']}/10")
                    
                    with col_b:
                        st.write(f"**{process2}:** {values['process2']}/10")
                    
                    with col_bar:
                        # Create a visual comparison bar
                        total = values['process1'] + values['process2']
                        width1 = (values['process1'] / 10) * 100
                        width2 = (values['process2'] / 10) * 100
                        
                        st.markdown(f"""
                        <div style="display: flex; height: 20px; background: #e5e7eb; border-radius: 10px; overflow: hidden;">
                            <div style="width: {width1}%; background: #3B82F6;"></div>
                            <div style="width: {width2}%; background: #10B981;"></div>
                        </div>
                        """, unsafe_allow_html=True)



def show_comparative_engine_page():
    """Enhanced comparative engine with matrix visualization"""
    
    st.title("Comparative Analysis Engine")
    st.markdown("Cross-tradition comparison and synthesis")
    
    # Initialize comparison state
    if 'comparison_data' not in st.session_state:
        st.session_state.comparison_data = {
            'selected_traditions': ['Stoic', 'Utilitarian'],
            'focus_dimensions': ['Ethical principles', 'Decision criteria'],
            'decision_context': ''
        }
    
    st.markdown("""
    ### Multi-Dimensional Comparison Framework
    
    Compare philosophical traditions across multiple analytical dimensions
    to generate integrated insights and balanced recommendations.
    """)
    
    # Main comparison interface
    col_config, col_visualization = st.columns([1, 2])
    
    with col_config:
        st.subheader("Comparison Configuration")
        
        # Tradition selection
        traditions = st.multiselect(
            "Select traditions to compare:",
            options=["Stoic", "Utilitarian", "Buddhist", "Virtue Ethics", "Deontological"],
            default=st.session_state.comparison_data['selected_traditions'],
            help="Select at least two traditions for meaningful comparison"
        )
        
        # Comparison dimensions
        dimensions = st.multiselect(
            "Comparison dimensions:",
            options=[
                "Ethical principles",
                "Decision criteria",
                "Outcome evaluation",
                "Virtue development",
                "Time perspective",
                "Stakeholder consideration",
                "Certainty handling",
                "Risk assessment"
            ],
            default=st.session_state.comparison_data['focus_dimensions']
        )
        
        # Decision context
        context = st.text_area(
            "Decision context (optional):",
            value=st.session_state.comparison_data['decision_context'],
            placeholder="Enter the specific decision or dilemma you want to analyze...",
            height=100
        )
        
        # Analysis depth
        depth = st.slider(
            "Analysis depth:",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Basic comparison, 5 = Comprehensive analysis with historical context"
        )
        
        # Update session state
        st.session_state.comparison_data.update({
            'selected_traditions': traditions,
            'focus_dimensions': dimensions,
            'decision_context': context
        })
        
        # Run comparison button
        if st.button("Run Comparative Analysis", type="primary", use_container_width=True):
            if len(traditions) >= 2 and len(dimensions) >= 1:
                st.session_state.run_comparison = True
                st.rerun()
            else:
                st.warning("Please select at least 2 traditions and 1 dimension")
    
    with col_visualization:
        if st.session_state.get('run_comparison', False) and len(traditions) >= 2:
            st.subheader("Comparative Analysis Results")
            
            # Create comparison matrix
            with st.spinner("Generating comparative analysis..."):
                # Simulate analysis
                import time
                time.sleep(2)
                
                # Display comparison matrix
                st.markdown("#### Tradition Comparison Matrix")
                
                # Create a pandas-like dataframe visualization
                comparison_results = {}
                
                for tradition in traditions:
                    tradition_scores = {}
                    for dimension in dimensions:
                        # Generate simulated scores
                        import random
                        score = random.uniform(0.5, 1.0) if dimension != "Ethical principles" else random.uniform(0.7, 1.0)
                        tradition_scores[dimension] = score
                    
                    comparison_results[tradition] = tradition_scores
                
                # Display as heatmap-like visualization
                import plotly.graph_objects as go
                
                # Prepare data for heatmap
                dimension_labels = dimensions
                tradition_labels = traditions
                
                scores_matrix = []
                for tradition in traditions:
                    row = [comparison_results[tradition][dim] for dim in dimensions]
                    scores_matrix.append(row)
                
                # Create heatmap
                fig = go.Figure(data=go.Heatmap(
                    z=scores_matrix,
                    x=dimension_labels,
                    y=tradition_labels,
                    colorscale='RdYlGn',
                    zmin=0,
                    zmax=1,
                    hoverongaps=False,
                    text=[[f"{score:.2f}" for score in row] for row in scores_matrix],
                    texttemplate="%{text}",
                    textfont={"size": 12}
                ))
                
                fig.update_layout(
                    title="Tradition Comparison Matrix",
                    xaxis_title="Dimensions",
                    yaxis_title="Traditions",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Generate insights
                st.markdown("#### Key Insights")
                
                # Calculate consensus and divergence
                insights = []
                
                for dimension in dimensions:
                    dim_scores = [comparison_results[t][dimension] for t in traditions]
                    avg_score = sum(dim_scores) / len(dim_scores)
                    
                    if avg_score > 0.8:
                        insights.append(f"**Strong consensus** on {dimension}")
                    elif avg_score > 0.6:
                        insights.append(f"**Moderate agreement** on {dimension}")
                    else:
                        insights.append(f"**Significant divergence** on {dimension}")
                
                for insight in insights:
                    st.write(f"- {insight}")
                
                # Generate recommendations
                st.markdown("#### Integrated Recommendations")
                
                if context:
                    st.write(f"**For decision context:** {context}")
                
                recommendations = [
                    "Consider a hybrid approach combining strengths from multiple traditions",
                    "Apply Stoic principles for aspects within your control",
                    "Use Utilitarian analysis for stakeholder impact assessment",
                    "Incorporate Buddhist mindfulness for emotional regulation during decision execution"
                ]
                
                for i, rec in enumerate(recommendations, 1):
                    st.write(f"{i}. {rec}")
                
                # Export options
                st.download_button(
                    label="Download Comparative Analysis",
                    data=str(comparison_results),
                    file_name="comparative_analysis.json",
                    mime="application/json"
                )
        
        else:
            st.info("Configure and run a comparison to see results here")
            
            # Show example comparison
            with st.expander("View Example Comparison"):
                st.markdown("""
                **Example: Career Change Decision**
                
                | Dimension | Stoic | Utilitarian | Buddhist |
                |-----------|-------|-------------|----------|
                | Focus | Virtue alignment | Overall happiness | Mindfulness & non-attachment |
                | Timeframe | Present focus | Future consequences | Timeless awareness |
                | Control | Dichotomy of control | Influencing outcomes | Non-attachment to outcomes |
                | Success Metric | Moral excellence | Net positive impact | Reduced suffering |
                
                **Integrated Insight:** Combine Stoic virtue ethics for personal development, 
                Utilitarian calculus for stakeholder impact, and Buddhist mindfulness for 
                emotional resilience throughout the transition.
                """)
    
    # Advanced comparison tools
    st.subheader("Advanced Comparison Tools")
    
    tab1, tab2, tab3 = st.tabs(["Weighted Analysis", "Historical Context", "Sensitivity Analysis"])
    
    with tab1:
        st.write("**Assign weights to different dimensions:**")
        
        weights = {}
        for dimension in dimensions:
            weight = st.slider(
                f"Weight for {dimension}:",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                help=f"Importance of {dimension} in the overall analysis"
            )
            weights[dimension] = weight
        
        if st.button("Apply Weights", key="apply_weights"):
            st.success("Weights applied to analysis!")
    
    with tab2:
        st.write("**Add historical context to traditions:**")
        
        historical_periods = {
            "Stoic": ["Ancient Greece (300 BCE)", "Roman Empire", "Modern Revival"],
            "Utilitarian": ["Enlightenment", "19th Century Reform", "Contemporary"],
            "Buddhist": ["Ancient India", "Spread to Asia", "Western Adoption"]
        }
        
        for tradition in traditions:
            period = st.selectbox(
                f"Historical period for {tradition}:",
                historical_periods.get(tradition, ["General"]),
                key=f"period_{tradition}"
            )
            
            if period != "General":
                st.info(f"Analyzing {tradition} tradition in {period} context")
    
    with tab3:
        st.write("**Test analysis sensitivity to different assumptions:**")
        
        sensitivity_factor = st.slider(
            "Sensitivity factor:",
            min_value=0.5,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="Adjust how sensitive the analysis is to parameter changes"
        )
        
        if st.button("Run Sensitivity Analysis", key="sensitivity_run"):
            with st.spinner("Testing sensitivity..."):
                time.sleep(1)
                st.success(f"Sensitivity analysis complete with factor {sensitivity_factor}")
                
                # Show sensitivity results
                st.metric(
                    "Result Stability",
                    "High" if sensitivity_factor < 1.2 else "Moderate",
                    delta="Stable" if sensitivity_factor < 1.2 else "Variable"
                )



def show_research_tools_page():
    """Enhanced research tools with template management"""
    
    st.title("Research and Documentation Tools")
    st.markdown("Academic paper generation and research utilities")
    
    # Template management system
    st.subheader("Research Templates")
    
    templates = {
        "Philosophical Analysis": {
            "description": "Template for analyzing decisions through philosophical frameworks",
            "sections": ["Abstract", "Introduction", "Methodology", "Analysis", "Conclusion", "References"],
            "word_count": 3000
        },
        "Process Study": {
            "description": "Template for mechanical process analysis papers",
            "sections": ["Abstract", "Theoretical Background", "Methodology", "Results", "Discussion", "Applications"],
            "word_count": 4000
        },
        "Comparative Ethics": {
            "description": "Template for cross-tradition ethical analysis",
            "sections": ["Abstract", "Literature Review", "Framework", "Case Studies", "Synthesis", "Implications"],
            "word_count": 5000
        },
        "Methodology Paper": {
            "description": "Template for methodological innovations in decision analysis",
            "sections": ["Abstract", "Problem Statement", "Proposed Method", "Validation", "Case Studies", "Limitations"],
            "word_count": 3500
        }
    }
    
    # Template selection and customization
    col1, col2 = st.columns([1, 2])
    
    with col1:
        selected_template = st.selectbox(
            "Select template:",
            options=list(templates.keys()),
            format_func=lambda x: f"{x} ({templates[x]['word_count']} words)"
        )
        
        template_info = templates[selected_template]
        
        st.write("**Template Details:**")
        st.write(template_info['description'])
        st.write(f"**Target length:** {template_info['word_count']} words")
        
        st.write("**Sections:**")
        for section in template_info['sections']:
            st.write(f"- {section}")
        
        # Quick actions
        if st.button("Create New from Template", key="create_new"):
            st.session_state.research_draft = {
                "template": selected_template,
                "title": f"New {selected_template} Paper",
                "sections": {section: "" for section in template_info['sections']}
            }
            st.success(f"Created new {selected_template} document")
    
    with col2:
        st.subheader("Paper Editor")
        
        # Check if we have a draft
        if 'research_draft' in st.session_state:
            draft = st.session_state.research_draft
            
            # Paper metadata
            title = st.text_input("Paper Title:", value=draft.get('title', ''))
            author = st.text_input("Author(s):", value=draft.get('author', ''))
            abstract = st.text_area("Abstract:", value=draft.get('abstract', ''), height=100)
            
            # Section editor
            st.subheader("Section Content")
            
            for section in template_info['sections']:
                with st.expander(section, expanded=section=="Introduction"):
                    content = st.text_area(
                        f"Content for {section}:",
                        value=draft['sections'].get(section, ''),
                        height=150 if section in ["Abstract", "Conclusion"] else 300,
                        key=f"section_{section}"
                    )
                    draft['sections'][section] = content
            
            # Update draft
            st.session_state.research_draft.update({
                'title': title,
                'author': author,
                'abstract': abstract
            })
            
            # Action buttons
            col_save, col_export, col_preview = st.columns(3)
            
            with col_save:
                if st.button("Save Draft", use_container_width=True):
                    st.toast("Draft saved!", icon="💾")
            
            with col_export:
                export_format = st.selectbox(
                    "Export as:",
                    ["LaTeX", "Word", "PDF", "Markdown", "HTML"],
                    key="export_format"
                )
                
                if st.button(f"Export as {export_format}", use_container_width=True):
                    # Simulate export
                    with st.spinner(f"Exporting as {export_format}..."):
                        time.sleep(1)
                        st.success(f"Exported as {export_format}!")
                        
                        # Provide download
                        st.download_button(
                            label=f"Download {export_format}",
                            data=f"{title}\n\n{abstract}\n\nPaper content...",
                            file_name=f"{title.replace(' ', '_')}.{export_format.lower()}",
                            mime={
                                "LaTeX": "text/x-tex",
                                "Word": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                "PDF": "application/pdf",
                                "Markdown": "text/markdown",
                                "HTML": "text/html"
                            }[export_format]
                        )
            
            with col_preview:
                if st.button("Generate Preview", use_container_width=True):
                    st.session_state.show_preview = True
            
            # Show preview if requested
            if st.session_state.get('show_preview', False):
                st.subheader("Paper Preview")
                
                preview_container = st.container()
                with preview_container:
                    st.markdown(f"# {title}")
                    st.markdown(f"*By {author}*" if author else "")
                    st.markdown("---")
                    st.markdown(f"**Abstract**\n\n{abstract}")
                    
                    for section in template_info['sections']:
                        if section != "Abstract" and draft['sections'].get(section):
                            st.markdown(f"## {section}")
                            st.markdown(draft['sections'][section])
        
        else:
            st.info("Select a template and click 'Create New' to start writing")
    
    # Additional research tools
    st.subheader("Research Utilities")
    
    tab_citations, tab_analysis, tab_collaboration = st.tabs([
        "Citation Manager", "Analysis Tools", "Collaboration"
    ])
    
    with tab_citations:
        st.write("**Manage references and citations**")
        
        # Citation database
        citations = st.session_state.get('citations', [])
        
        # Add new citation
        with st.form("add_citation"):
            st.write("Add New Citation")
            
            col_type, col_year = st.columns(2)
            
            with col_type:
                citation_type = st.selectbox(
                    "Type:",
                    ["Book", "Journal Article", "Conference Paper", "Website", "Other"]
                )
            
            with col_year:
                year = st.number_input("Year:", min_value=1900, max_value=2100, value=2024)
            
            author = st.text_input("Author(s):")
            title = st.text_input("Title:")
            journal = st.text_input("Journal/Publication:")
            
            if st.form_submit_button("Add Citation"):
                new_citation = {
                    'type': citation_type,
                    'year': year,
                    'author': author,
                    'title': title,
                    'journal': journal
                }
                citations.append(new_citation)
                st.session_state.citations = citations
                st.success("Citation added!")
        
        # Display citations
        if citations:
            st.write("**Your Citations:**")
            for idx, citation in enumerate(citations):
                with st.expander(f"{citation['author']} ({citation['year']}) - {citation['title']}"):
                    st.write(citation)
        
        # Export citations
        if citations and st.button("Export Citations (BibTeX)"):
            bibtex_entries = []
            for citation in citations:
                entry = f"""@article{{{citation['author'].split()[0].lower()}{citation['year']},
  author = {{{citation['author']}}},
  title = {{{citation['title']}}},
  journal = {{{citation['journal']}}},
  year = {{{citation['year']}}}
}}"""
                bibtex_entries.append(entry)
            
            st.download_button(
                label="Download BibTeX",
                data="\n\n".join(bibtex_entries),
                file_name="citations.bib",
                mime="text/x-bibtex"
            )
    
    with tab_analysis:
        st.write("**Statistical and analytical tools**")
        
        # Data upload for analysis
        uploaded_file = st.file_uploader(
            "Upload research data (CSV or Excel):",
            type=['csv', 'xlsx', 'xls']
        )
        
        if uploaded_file:
            import pandas as pd
            
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                st.success(f"Data loaded: {len(df)} rows, {len(df.columns)} columns")
                
                # Quick analysis
                st.write("**Data Preview:**")
                st.dataframe(df.head())
                
                # Analysis options
                analysis_type = st.selectbox(
                    "Select analysis:",
                    ["Descriptive Statistics", "Correlation Analysis", "Regression", "Hypothesis Testing"]
                )
                
                if analysis_type == "Descriptive Statistics":
                    st.write(df.describe())
                
                elif analysis_type == "Correlation Analysis":
                    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                    if len(numeric_cols) >= 2:
                        corr_matrix = df[numeric_cols].corr()
                        st.write("Correlation Matrix:")
                        st.dataframe(corr_matrix)
                        
                        # Visualize
                        try:
                            import plotly.figure_factory as ff
                            fig = ff.create_annotated_heatmap(
                                z=corr_matrix.values,
                                x=list(corr_matrix.columns),
                                y=list(corr_matrix.index),
                                colorscale='RdBu',
                                showscale=True
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        except:
                            st.write("Correlation heatmap requires plotly")
                
            except Exception as e:
                st.error(f"Error loading file: {str(e)}")
    
    with tab_collaboration:
        st.write("**Collaboration and sharing tools**")
        
        # Share settings
        share_level = st.radio(
            "Sharing level:",
            ["Private", "Shared with team", "Public read-only", "Public editable"]
        )
        
        # Collaborator management
        collaborators = st.multiselect(
            "Add collaborators:",
            ["user1@example.com", "user2@example.com", "user3@example.com"]
        )
        
        if collaborators:
            st.write(f"**Collaborators:** {', '.join(collaborators)}")
        
        # Version history
        if st.button("View Version History"):
            st.info("Version history would show previous edits and collaborators' changes")
        
        # Comments and feedback
        comment = st.text_area("Add comment or feedback:")
        if st.button("Post Comment"):
            if comment:
                st.success("Comment posted!")
                # In a real app, this would be saved to a database database



def show_configuration_page():
    """Enhanced configuration page with persistence"""
    
    st.title("Platform Configuration")
    st.markdown("System settings and customization options")
    
    # Tabbed configuration interface
    tab_general, tab_api, tab_appearance, tab_advanced = st.tabs([
        "General", "API Settings", "Appearance", "Advanced"
    ])
    
    with tab_general:
        st.subheader("General Settings")
        
        # Application settings
        app_language = st.selectbox(
            "Interface Language:",
            ["English", "Spanish", "French", "German", "Chinese", "Japanese"],
            help="Language for user interface elements"
        )
        
        date_format = st.selectbox(
            "Date Format:",
            ["YYYY-MM-DD", "MM/DD/YYYY", "DD/MM/YYYY", "Month DD, YYYY"]
        )
        
        timezone = st.selectbox(
            "Timezone:",
            ["UTC", "US/Eastern", "US/Pacific", "Europe/London", "Asia/Tokyo"]
        )
        
        # Default analysis settings
        st.subheader("Default Analysis Settings")
        
        default_tradition = st.selectbox(
            "Default Philosophical Tradition:",
            ["Stoic", "Utilitarian", "Buddhist", "Auto-select based on context"]
        )
        
        auto_save = st.checkbox(
            "Enable auto-save",
            value=True,
            help="Automatically save analysis drafts"
        )
        
        auto_save_interval = st.slider(
            "Auto-save interval (minutes):",
            min_value=1,
            max_value=30,
            value=5,
            disabled=not auto_save
        )
        
        # Notification settings
        st.subheader("Notifications")
        
        notify_completion = st.checkbox(
            "Notify when analysis completes",
            value=True
        )
        
        notify_errors = st.checkbox(
            "Notify on errors",
            value=True
        )
        
        email_notifications = st.checkbox(
            "Enable email notifications",
            value=False
        )
        
        if email_notifications:
            email_address = st.text_input("Notification email:")
    
    with tab_api:
        st.subheader("API Configuration")
        
        # API endpoints
        api_base_url = st.text_input(
            "API Base URL:",
            value=st.session_state.config.get('api_base_url', 'http://localhost:8000'),
            help="Base URL for the decision intelligence API"
        )
        
        # Test connection
        col_test, col_status = st.columns([3, 1])
        with col_test:
            if st.button("Test API Connection", key="test_api"):
                # Simulate API test
                with st.spinner("Testing connection..."):
                    import time
                    time.sleep(1)
                    
                    # Mock response
                    st.session_state.api_connected = True
                    st.success("API connection successful!")
        
        with col_status:
            status = "Connected" if st.session_state.api_connected else "Disconnected"
            color = "green" if st.session_state.api_connected else "red"
            st.markdown(f"Status: <span style='color:{color}'>{status}</span>", 
                       unsafe_allow_html=True)
        
        # API timeout settings
        api_timeout = st.number_input(
            "API Timeout (seconds):",
            min_value=5,
            max_value=120,
            value=st.session_state.config.get('api_timeout', 30),
            help="Maximum time to wait for API responses"
        )
        
        # Retry settings
        max_retries = st.number_input(
            "Maximum retries:",
            min_value=0,
            max_value=10,
            value=st.session_state.config.get('max_retries', 3)
        )
        
        retry_delay = st.number_input(
            "Retry delay (seconds):",
            min_value=1,
            max_value=10,
            value=st.session_state.config.get('retry_delay', 2)
        )
        
        # API caching
        enable_cache = st.checkbox(
            "Enable response caching",
            value=st.session_state.config.get('enable_cache', True)
        )
        
        if enable_cache:
            cache_ttl = st.number_input(
                "Cache TTL (minutes):",
                min_value=1,
                max_value=1440,
                value=st.session_state.config.get('cache_ttl', 60)
            )
    
    with tab_appearance:
        st.subheader("Appearance Settings")
        
        # Theme selection
        theme = st.selectbox(
            "Theme:",
            ["Light", "Dark", "System Default"],
            index=["Light", "Dark", "System Default"].index(
                st.session_state.config.get('theme', 'Light')
            )
        )
        
        # Color scheme
        primary_color = st.color_picker(
            "Primary Color:",
            value=st.session_state.config.get('primary_color', '#1E3A8A')
        )
        
        secondary_color = st.color_picker(
            "Secondary Color:",
            value=st.session_state.config.get('secondary_color', '#2563EB')
        )
        
        # Layout options
        layout_mode = st.radio(
            "Layout Mode:",
            ["Wide", "Centered", "Compact"],
            horizontal=True
        )
        
        # Font settings
        font_family = st.selectbox(
            "Font Family:",
            ["System Default", "Arial", "Georgia", "Helvetica", "Times New Roman"]
        )
        
        font_size = st.select_slider(
            "Base Font Size:",
            options=["Small", "Medium", "Large"],
            value=st.session_state.config.get('font_size', 'Medium')
        )
        
        # Preview
        st.subheader("Preview")
        st.markdown("""
        <div style="padding: 20px; border-radius: 10px; background: #f0f0f0;">
            <h3 style="color: {primary_color};">Sample Header</h3>
            <p style="color: {secondary_color};">Sample text with secondary color</p>
            <button style="background: {primary_color}; color: white; padding: 10px; border: none; border-radius: 5px;">
                Sample Button
            </button>
        </div>
        """.format(primary_color=primary_color, secondary_color=secondary_color), 
        unsafe_allow_html=True)
    
    with tab_advanced:
        st.subheader("Advanced Settings")
        
        # Debug mode
        debug_mode = st.checkbox(
            "Enable debug mode",
            value=st.session_state.get('debug_mode', False),
            help="Show detailed error messages and logs"
        )
        
        # Performance settings
        st.subheader("Performance")
        
        auto_refresh = st.checkbox(
            "Enable auto-refresh",
            value=st.session_state.config.get('auto_refresh', False)
        )
        
        if auto_refresh:
            refresh_interval = st.selectbox(
                "Refresh interval:",
                ["30 seconds", "1 minute", "5 minutes", "15 minutes"]
            )
        
        # Data management
        st.subheader("Data Management")
        
        data_retention = st.selectbox(
            "Data retention period:",
            ["30 days", "90 days", "1 year", "Indefinite"]
        )
        
        if st.button("Clear Local Cache", key="clear_cache"):
            st.session_state.module_cache = {}
            st.success("Local cache cleared!")
        
        # Export/Import settings
        st.subheader("Export/Import")
        
        default_export_format = st.selectbox(
            "Default export format:",
            ["JSON", "CSV", "Excel", "PDF"]
        )
        
        # Backup settings
        enable_auto_backup = st.checkbox(
            "Enable automatic backups",
            value=False
        )
        
        if enable_auto_backup:
            backup_interval = st.selectbox(
                "Backup interval:",
                ["Daily", "Weekly", "Monthly"]
            )
    
    # Save configuration
    st.markdown("---")
    col_save, col_reset, col_export = st.columns(3)
    
    with col_save:
        if st.button("Save Configuration", type="primary", use_container_width=True):
            # Update configuration
            st.session_state.config.update({
                'theme': theme,
                'primary_color': primary_color,
                'secondary_color': secondary_color,
                'font_size': font_size,
                'api_base_url': api_base_url,
                'api_timeout': api_timeout,
                'auto_refresh': auto_refresh,
                'default_tradition': default_tradition
            })
            
            st.session_state.debug_mode = debug_mode
            
            st.success("Configuration saved!")
            st.info("Some changes may require restarting the application.")
    
    with col_reset:
        if st.button("Reset to Defaults", use_container_width=True):
            st.session_state.config = {
                'theme': 'Light',
                'auto_refresh': False,
                'default_tradition': 'Stoic',
                'api_base_url': 'http://localhost:8000',
                'api_timeout': 30
            }
            st.session_state.debug_mode = False
            st.success("Configuration reset to defaults!")
            st.rerun()
    
    with col_export:
        if st.button("Export Configuration", use_container_width=True):
            import json
            config_json = json.dumps(st.session_state.config, indent=2)
            
            st.download_button(
                label="Download Config",
                data=config_json,
                file_name="dashboard_config.json",
                mime="application/json"
            )


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
            result = mod.main()
            # If main() returns a tuple, use it; otherwise return success
            return result if isinstance(result, tuple) and len(result) == 2 else (True, None)
        else:
            attempts.append(f"Imported decisions.dashboard.pages.{module_name} but no main() found.")
    except Exception:
        attempts.append(traceback.format_exc())

    # Attempt relative import (if this module is itself within a package)
    try:
        mod = __import__(f".pages.{module_name}", globals(), locals(), ["*"])
        if hasattr(mod, "main"):
            result = mod.main()
            # If main() returns a tuple, use it; otherwise return success
            return result if isinstance(result, tuple) and len(result) == 2 else (True, None)
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
    try:
        # Try new API first (Streamlit >= 1.28)
        query_params = st.query_params
        requested_page = None
        if "page" in query_params:
            raw = query_params.get("page", "") or ""
            requested_page = _query_to_label.get(raw.lower())
    except AttributeError:
        # Fallback to deprecated API for older Streamlit versions
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
            st.info("Creating default home page...")
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


class NavigationManager:
    """Manages page navigation and routing"""
    
    PAGE_MAPPINGS = {
        'home': {
            'function': show_home_page,
            'sidebar_label': 'Home',
            'icon': '🏠'
        },
        'analysis': {
            'function': show_analysis_page,
            'sidebar_label': 'Philosophical Analysis',
            'icon': '🔍'
        },
        'mechanical_processes': {
            'function': show_mechanical_processes_page,
            'sidebar_label': 'Mechanical Processes',
            'icon': '🔧'
        },
        'comparative_engine': {
            'function': show_comparative_engine_page,
            'sidebar_label': 'Comparative Engine',
            'icon': '📊'
        },
        'research_tools': {
            'function': show_research_tools_page,
            'sidebar_label': 'Research Tools',
            'icon': '📚'
        },
        'configuration': {
            'function': show_configuration_page,
            'sidebar_label': 'Configuration',
            'icon': '⚙️'
        }
    }
    
    @staticmethod
    def create_sidebar():
        """Create sidebar navigation with current page highlighting"""
        
        st.sidebar.title("Navigation")
        st.sidebar.markdown("---")
        
        # Create navigation buttons
        for page_id, page_info in NavigationManager.PAGE_MAPPINGS.items():
            label = f"{page_info['icon']} {page_info['sidebar_label']}"
            
            # Highlight current page
            is_current = st.session_state.page == page_id
            button_type = "primary" if is_current else "secondary"
            
            if st.sidebar.button(
                label,
                key=f"nav_{page_id}",
                use_container_width=True,
                type=button_type
            ):
                st.session_state.page = page_id
                st.rerun()
        
        st.sidebar.markdown("---")
        
        # Status indicator
        st.sidebar.subheader("System Status")
        
        api_status = "Connected" if st.session_state.api_connected else "Disconnected"
        api_color = "🟢" if st.session_state.api_connected else "🔴"
        
        st.sidebar.write(f"API: {api_color} {api_status}")
        
        # Quick actions
        st.sidebar.markdown("---")
        st.sidebar.subheader("Quick Actions")
        
        if st.sidebar.button("New Analysis", icon="📝", use_container_width=True):
            st.session_state.page = 'analysis'
            st.rerun()
        
        if st.sidebar.button("Clear Cache", icon="🗑️", use_container_width=True):
            st.session_state.module_cache = {}
            st.sidebar.success("Cache cleared!")
        
        # Debug toggle (only in debug mode)
        if st.session_state.get('debug_mode', False):
            st.sidebar.markdown("---")
            st.sidebar.subheader("Debug")
            
            if st.sidebar.button("Show Session State", icon="🐛", use_container_width=True):
                st.write(st.session_state)


def main():
    """Main application entry point"""
    
    # Initialize session state
    DashboardState.initialize()
    
    # Setup navigation
    NavigationManager.create_sidebar()
    
    # Display current page
    current_page = st.session_state.page
    
    if current_page in NavigationManager.PAGE_MAPPINGS:
        page_info = NavigationManager.PAGE_MAPPINGS[current_page]
        
        # Try to load external module first
        if current_page != 'home':  # home has special handling in PageLoader
            ran = PageLoader.execute_page(
                current_page,
                page_info['function']
            )
        else:
            # For home page, try to load external module with run() wrapper
            module = PageLoader.load_page_module('home')
            if module and hasattr(module, 'run'):
                # Call run() which returns (ran, err) tuple
                ran, err = module.run()
                if not ran and err:
                    st.error(f"Home page module failed: {err}")
                    show_home_page()
            elif module and hasattr(module, 'main'):
                # Fallback to main() if run() doesn't exist
                module.main()
            else:
                # Fallback to built-in home page
                ran, err = _try_import_and_run('home')
                if not ran:
                    if err:
                        st.error(f"Home page module import failed; showing built-in home page. Details:\n{err}")
                    show_home_page()
    else:
        # Default to home page
        st.session_state.page = 'home'
        st.rerun()
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.caption("Comparative Decision Intelligence Platform")
    
    with col2:
        st.caption("Version 1.0.0")
    
    with col3:
        if st.session_state.get('debug_mode', False):
            st.caption(f"Page: {st.session_state.page}")


if __name__ == "__main__":
    main()

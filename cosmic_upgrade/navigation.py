"""
Cosmic Navigation - Sidebar navigation with cosmic styling
"""

import streamlit as st


def create_cosmic_sidebar():
    """
    Create a cosmic-themed sidebar with decorative header, navigation buttons,
    and metrics block.
    
    This function renders:
    - A decorative cosmic header in the sidebar
    - Navigation buttons that set st.session_state.cosmic_page
    - A small metrics block showing cosmic theme status
    
    Returns:
        None
    """
    try:
        # Cosmic Sidebar Header
        st.sidebar.markdown("""
        <div class="cosmic-sidebar-header">
            <h2>🌌 Cosmic Mode</h2>
            <p style="color: #b39ddb; margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                Enhanced with starlight
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Section
        st.sidebar.markdown("### 🚀 Cosmic Navigation")
        
        # Initialize cosmic_page if not exists
        if 'cosmic_page' not in st.session_state:
            st.session_state.cosmic_page = 'home'
        
        # Navigation buttons with cosmic styling
        cosmic_pages = {
            'home': {'label': '🏠 Home', 'icon': '🏠'},
            'analysis': {'label': '🔍 Analysis', 'icon': '🔍'},
            'processes': {'label': '⚙️ Processes', 'icon': '⚙️'},
            'research': {'label': '📚 Research', 'icon': '📚'},
        }
        
        for page_key, page_info in cosmic_pages.items():
            # Highlight current page
            is_active = st.session_state.cosmic_page == page_key
            button_class = "cosmic-nav-button active" if is_active else "cosmic-nav-button"
            
            if st.sidebar.button(
                page_info['label'],
                key=f"cosmic_nav_{page_key}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.cosmic_page = page_key
                st.rerun()
        
        # Cosmic Metrics
        st.sidebar.markdown("---")
        st.sidebar.markdown("### ✨ Cosmic Metrics")
        
        # Theme Status Metric
        st.sidebar.markdown("""
        <div class="cosmic-metric">
            <h3>Theme Status</h3>
            <div class="value">Active ✨</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation Count Metric
        nav_count = st.session_state.get('cosmic_nav_count', 0)
        st.sidebar.markdown(f"""
        <div class="cosmic-metric">
            <h3>Page Views</h3>
            <div class="value">{nav_count} 🌟</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Cosmic Mode Toggle Info
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        <div style="background: rgba(126, 87, 194, 0.2); border-radius: 8px; padding: 1rem; margin-top: 1rem;">
            <p style="color: #b39ddb; margin: 0; font-size: 0.85rem; text-align: center;">
                🌌 Cosmic mode is a non-breaking overlay theme
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Increment navigation counter
        if 'cosmic_nav_count' not in st.session_state:
            st.session_state.cosmic_nav_count = 0
        st.session_state.cosmic_nav_count += 1
        
    except Exception as e:
        st.sidebar.warning(f"Cosmic navigation error: {e}")

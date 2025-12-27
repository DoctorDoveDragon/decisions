"""
Cosmic Upgrade - Main upgrade function for existing dashboard
"""

import sys
import streamlit as st


def upgrade_existing_dashboard():
    """
    Upgrade the existing dashboard with cosmic theme overlay.
    
    This function:
    1. Checks if streamlit is available in sys.modules
    2. Applies the cosmic theme via theme.apply_cosmic_theme()
    3. Ensures sidebar is added only once via st.session_state.cosmic_sidebar_added
    4. Calls navigation.create_cosmic_sidebar()
    5. Inserts a cosmic header in main content area
    
    Returns:
        bool: True on success, False on failure (with warning)
    """
    try:
        # Check if Streamlit is available
        if 'streamlit' not in sys.modules:
            st.warning("⚠️ Streamlit not found in sys.modules. Cosmic theme requires Streamlit.")
            return False
        
        # Import cosmic modules
        from cosmic_upgrade import theme, navigation
        
        # Apply cosmic theme CSS
        theme_applied = theme.apply_cosmic_theme()
        
        if not theme_applied:
            st.warning("⚠️ Could not apply cosmic theme CSS.")
            return False
        
        # Add cosmic sidebar (only once per session)
        if 'cosmic_sidebar_added' not in st.session_state:
            st.session_state.cosmic_sidebar_added = False
        
        if not st.session_state.cosmic_sidebar_added:
            navigation.create_cosmic_sidebar()
            st.session_state.cosmic_sidebar_added = True
        
        # Add cosmic header to main content
        st.markdown("""
        <div class="cosmic-header">
            <h1>🌌 Cosmic Decision Intelligence</h1>
            <p>Navigate the universe of philosophical wisdom with stellar clarity</p>
        </div>
        
        <div class="cosmic-background"></div>
        <div class="cosmic-stars"></div>
        """, unsafe_allow_html=True)
        
        # Success indicator
        return True
        
    except ImportError as e:
        st.warning(f"⚠️ Could not import cosmic modules: {e}")
        return False
    except Exception as e:
        st.warning(f"⚠️ Cosmic upgrade failed: {e}")
        return False

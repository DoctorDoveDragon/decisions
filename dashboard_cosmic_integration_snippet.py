"""
Cosmic Theme Integration Snippet for dashboard/app.py

Copy this code and add it to the TOP of dashboard/app.py
(BEFORE the st.set_page_config call)

This is a safe, non-breaking integration that:
- Only activates if cosmic_upgrade is available
- Shows a toast notification when activated
- Gracefully falls back if not available
- Does not modify any existing functionality
"""

# ============================================================
# Cosmic Theme Overlay (optional, non-breaking)
# ============================================================
try:
    from cosmic_upgrade.upgrade import upgrade_existing_dashboard
    
    # Attempt to upgrade with cosmic theme
    cosmic_active = upgrade_existing_dashboard()
    
    # Show success notification if cosmic mode is active
    if cosmic_active:
        import streamlit as st
        st.toast("🌌 Cosmic mode activated!", icon="✨")
        
except ImportError:
    # Cosmic upgrade module not available, continue normally
    pass
except Exception as e:
    # Any other error, log and continue normally
    import streamlit as st
    st.sidebar.info(f"Cosmic theme not activated: {e}")
# ============================================================
# End of Cosmic Theme Integration
# ============================================================


# Your existing dashboard code continues below...
# (st.set_page_config and other imports)

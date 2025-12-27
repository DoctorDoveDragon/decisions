"""
Cosmic Verification - Deployment verification utility
"""

import streamlit as st
import os
from pathlib import Path


def verify_deployment():
    """
    Verify that the cosmic_upgrade module is properly deployed.
    
    This function:
    1. Checks for cosmic_upgrade directory existence
    2. Verifies required files are present
    3. Attempts to import the theme module
    4. Displays results with st.success / st.error
    5. Shows st.balloons() on successful verification
    
    Returns:
        None (displays results in Streamlit)
    """
    st.title("🌌 Cosmic Upgrade Verification")
    st.markdown("---")
    
    # Track verification status
    all_checks_passed = True
    
    # Check 1: Verify cosmic_upgrade directory exists
    st.subheader("📁 Directory Check")
    cosmic_dir = Path(__file__).parent
    
    if cosmic_dir.exists() and cosmic_dir.is_dir():
        st.success(f"✅ cosmic_upgrade directory found: {cosmic_dir}")
    else:
        st.error("❌ cosmic_upgrade directory not found")
        all_checks_passed = False
    
    # Check 2: Verify required files
    st.subheader("📄 Required Files Check")
    
    required_files = [
        '__init__.py',
        'theme.py',
        'navigation.py',
        'upgrade.py',
        'verify.py'
    ]
    
    missing_files = []
    
    for file_name in required_files:
        file_path = cosmic_dir / file_name
        if file_path.exists():
            st.success(f"✅ {file_name} found")
        else:
            st.error(f"❌ {file_name} missing")
            missing_files.append(file_name)
            all_checks_passed = False
    
    # Check 3: Try importing theme module
    st.subheader("🎨 Theme Import Check")
    
    try:
        from cosmic_upgrade import theme
        st.success("✅ Successfully imported cosmic_upgrade.theme")
        
        # Verify COSMIC_CSS exists
        if hasattr(theme, 'COSMIC_CSS'):
            st.success("✅ COSMIC_CSS string found")
        else:
            st.error("❌ COSMIC_CSS string not found in theme module")
            all_checks_passed = False
        
        # Verify apply_cosmic_theme exists
        if hasattr(theme, 'apply_cosmic_theme'):
            st.success("✅ apply_cosmic_theme() function found")
        else:
            st.error("❌ apply_cosmic_theme() function not found")
            all_checks_passed = False
            
    except ImportError as e:
        st.error(f"❌ Failed to import theme module: {e}")
        all_checks_passed = False
    
    # Check 4: Try importing navigation module
    st.subheader("🧭 Navigation Import Check")
    
    try:
        from cosmic_upgrade import navigation
        st.success("✅ Successfully imported cosmic_upgrade.navigation")
        
        if hasattr(navigation, 'create_cosmic_sidebar'):
            st.success("✅ create_cosmic_sidebar() function found")
        else:
            st.error("❌ create_cosmic_sidebar() function not found")
            all_checks_passed = False
            
    except ImportError as e:
        st.error(f"❌ Failed to import navigation module: {e}")
        all_checks_passed = False
    
    # Check 5: Try importing upgrade module
    st.subheader("⬆️ Upgrade Import Check")
    
    try:
        from cosmic_upgrade import upgrade
        st.success("✅ Successfully imported cosmic_upgrade.upgrade")
        
        if hasattr(upgrade, 'upgrade_existing_dashboard'):
            st.success("✅ upgrade_existing_dashboard() function found")
        else:
            st.error("❌ upgrade_existing_dashboard() function not found")
            all_checks_passed = False
            
    except ImportError as e:
        st.error(f"❌ Failed to import upgrade module: {e}")
        all_checks_passed = False
    
    # Check 6: Verify module metadata
    st.subheader("📋 Module Metadata Check")
    
    try:
        import cosmic_upgrade
        
        if hasattr(cosmic_upgrade, '__version__'):
            st.success(f"✅ Version: {cosmic_upgrade.__version__}")
        else:
            st.warning("⚠️ __version__ not defined in __init__.py")
        
        if hasattr(cosmic_upgrade, '__author__'):
            st.success(f"✅ Author: {cosmic_upgrade.__author__}")
        else:
            st.warning("⚠️ __author__ not defined in __init__.py")
            
    except ImportError as e:
        st.error(f"❌ Failed to import cosmic_upgrade: {e}")
        all_checks_passed = False
    
    # Final verdict
    st.markdown("---")
    st.subheader("🎯 Verification Result")
    
    if all_checks_passed:
        st.success("🎉 All verification checks passed!")
        st.balloons()
        
        st.markdown("""
        ### ✨ Next Steps:
        
        1. **Integrate with dashboard**: Add the integration snippet to `dashboard/app.py`
        2. **Test the theme**: Run `streamlit run dashboard/app.py`
        3. **Verify visuals**: Check that cosmic styling appears correctly
        
        See `dashboard_cosmic_integration_snippet.py` for integration example.
        """)
    else:
        st.error("❌ Some verification checks failed. Please review the errors above.")
        
        if missing_files:
            st.markdown("### Missing Files:")
            for file in missing_files:
                st.markdown(f"- {file}")
    
    # Show deployment info
    st.markdown("---")
    st.subheader("ℹ️ Deployment Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Checks", len(required_files) + 5)
    
    with col2:
        status = "Passed ✅" if all_checks_passed else "Failed ❌"
        st.metric("Status", status)


if __name__ == "__main__":
    verify_deployment()

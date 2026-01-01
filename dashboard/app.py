"""
Main Dashboard with Navigation - Enhanced Version

Dashboard entrypoint with safe CSS injection and defensive page/module loading.

This file:
- Loads CSS from a static file and injects via st.markdown(...)
- Provides a defensive page-loading helper `_try_import_and_run`
- Uses a defensive home-page loading branch so the app tolerates modules that:
    * return None
    * return a (ran, err) tuple
    * are modules exposing run() or main()
- Falls back to a built-in home UI when external home page fails.
"""

import traceback
import streamlit as st
import os
import sys
import importlib
import types
from typing import Optional, Tuple
from pathlib import Path
import logging

# Add parent directory to path to import modules (only if not already present)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

logger = logging.getLogger(__name__)

# The CSS was moved to a static file to avoid a SyntaxError when parsing Python source.
# This keeps compatibility: code importing CUSTOM_CSS will still get the CSS text.
_css_path = Path(__file__).resolve().parents[0] / "static" / "css" / "custom.css"
try:
    _css_content = _css_path.read_text(encoding="utf-8")
    CUSTOM_CSS = f"<style>\n{_css_content}\n</style>"
except Exception:
    logger.exception("Could not read custom CSS from %s", _css_path)
    CUSTOM_CSS = ""

# ----------------------------
# Page config and CSS injection
# ----------------------------
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

# Apply custom CSS styling (unsafe_allow_html required for style injection)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


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

# Inject CSS into Streamlit
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------
# Helper functions for page loading
# ---------------------------------
def _try_import_and_run(name: str) -> Tuple[bool, Optional[str]]:
    """
    Try to import a front-end module by name and execute its run()/main() entrypoint.
    Returns (ran: bool, err: Optional[str])
    """
    possible_module_paths = [
        f"dashboard.frontend.{name}",
        f"dashboard.pages.{name}",
        f"frontend.{name}",
        name,
    ]
    last_err = None
    for module_path in possible_module_paths:
        try:
            module = importlib.import_module(module_path)
        except Exception as e:
            last_err = traceback.format_exc()
            continue

        # If the loader returned a tuple directly from some other mechanism, treat appropriately
        # but here we have a module object
        try:
            # prefer run()
            if hasattr(module, "run") and callable(getattr(module, "run")):
                res = module.run()
                if isinstance(res, tuple) and len(res) == 2:
                    return res
                return True, None
            # fallback to main()
            if hasattr(module, "main") and callable(getattr(module, "main")):
                res = module.main()
                if isinstance(res, tuple) and len(res) == 2:
                    return res
                return True, None
            # If module has UI code on import (side-effects), consider that a success
            return True, None
        except Exception:
            return False, traceback.format_exc()

    # If we reach here no import succeeded
    return False, last_err or f"Could not import module for {name}"


def show_built_in_home():
    """Render a simple built-in home page (fallback)."""
    st.markdown('<h1 class="main-header">🧠 Comparative Decision Intelligence Platform</h1>', unsafe_allow_html=True)
    st.markdown(
        """
        ## 🎯 Integrated Understanding System

        This platform combines **philosophical wisdom** with **mechanical process analysis**
        to provide comprehensive decision intelligence.

        Use the sidebar to navigate pages. If an external 'home' module is present it will be used.
        """)
    st.divider()
    st.subheader("Quick Start")
    st.markdown(
        """
        - Start the API server: `python -m api.server`
        - Start the dashboard: `streamlit run dashboard/app.py`
        """
    )


# --------------------------
# Sidebar navigation (basic)
# --------------------------
with st.sidebar:
    st.markdown("<h3>🌌 COSMIC NAVIGATION</h3>", unsafe_allow_html=True)
    nav_options = [
        ("🏠 COSMIC DASHBOARD", "home"),
        ("🔮 PHILOSOPHICAL ORACLE", "philosophy"),
        ("⚙️ MECHANICAL COSMOS", "mechanical"),
        ("📊 QUANTUM COMPARISONS", "comparisons"),
        ("📚 COSMIC ARCHIVES", "archives"),
        ("⚡ ENERGY FLOW", "energy"),
    ]

    # initialize session state if needed
    if "page" not in st.session_state:
        st.session_state.page = "home"

    for label, page_id in nav_options:
        is_active = st.session_state.get("page", "home") == page_id
        if st.button(label, key=f"nav-{page_id}", use_container_width=True):
            st.session_state.page = page_id
            st.experimental_rerun()

# --------------------------
# Page dispatch / rendering
# --------------------------
current_page = st.session_state.get("page", "home")

# If an external PageLoader exists in the project, prefer it; otherwise use fallback import routine.
PageLoader = globals().get("PageLoader", None)

if current_page != "home":
    # Try to delegate to PageLoader.execute_page if available; otherwise try our import fallback
    if PageLoader and hasattr(PageLoader, "execute_page"):
        try:
            ran = PageLoader.execute_page(current_page)
        except Exception:
            st.error("Error executing page via PageLoader:")
            st.error(traceback.format_exc())
            show_built_in_home()
    else:
        ran, err = _try_import_and_run(current_page)
        if not ran:
            if err:
                st.error(f"Page import failed: {err}")
            show_built_in_home()
else:
    # Defensive handling for home page (many apps treat home specially)
    ran, err = False, None

    # If PageLoader.load_page_module exists, it may return:
    #  - a module object
    #  - a (ran, err) tuple
    #  - None
    if PageLoader and hasattr(PageLoader, "load_page_module"):
        try:
            loader_result = PageLoader.load_page_module("home")
        except Exception:
            loader_result = None
            loader_exc = traceback.format_exc()
            # preserve exception text for later if needed
            err = loader_exc

        # If loader returned a tuple directly
        if isinstance(loader_result, tuple) and len(loader_result) == 2:
            ran, err = loader_result
        # If loader returned a module object, attempt to call its entrypoints
        elif isinstance(loader_result, types.ModuleType):
            module = loader_result
            # try module.run() / module.main() defensively
            if hasattr(module, "run") and callable(getattr(module, "run")):
                try:
                    res = module.run()
                except Exception:
                    ran, err = False, traceback.format_exc()
                else:
                    if isinstance(res, tuple) and len(res) == 2:
                        ran, err = res
                    else:
                        ran, err = True, None
            elif hasattr(module, "main") and callable(getattr(module, "main")):
                try:
                    res = module.main()
                except Exception:
                    ran, err = False, traceback.format_exc()
                else:
                    if isinstance(res, tuple) and len(res) == 2:
                        ran, err = res
                    else:
                        ran, err = True, None
            else:
                # Fallback to built-in home page
                ran, err = _try_import_and_run('home')
                if not ran:
                    if err:
                        st.error(f"Home page module import failed; showing built-in home page. Details:\n{err}")
                    show_home_page()
                ran, err = False, "Loaded home module has no run() or main() entrypoint"
        else:
            # loader_result is None or unexpected; try fallback import routine
            if err is None:
                # err may already contain loader exception text; otherwise try import fallback
                ran, err = _try_import_and_run("home")
    else:
        # No PageLoader available; use our fallback import & run helper
        ran, err = _try_import_and_run("home")

    if not ran:
        if err:
            st.error(f"Home page module import failed; showing built-in home page. Details:\n{err}")
        show_built_in_home()

# --------------------------
# Footer
# --------------------------
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("Comparative Decision Intelligence Platform")
with col2:
    st.caption("Version 1.0.0")
with col3:
    st.caption("© 2025")

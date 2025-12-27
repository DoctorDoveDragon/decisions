"""
Cosmic Theme - CSS styling for cosmic overlay
"""

import streamlit as st

COSMIC_CSS = """
<style>
    /* Cosmic Theme Overlay - Additive Styles */
    
    /* Cosmic Background Animation */
    @keyframes cosmic-pulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.6; }
    }
    
    @keyframes stars-twinkle {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    /* Cosmic Background Layer */
    .cosmic-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #1a0033 0%, #0a0015 50%, #000428 100%);
        z-index: -1;
        pointer-events: none;
    }
    
    /* Starfield Effect */
    .cosmic-stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, transparent),
            radial-gradient(2px 2px at 60px 70px, #fff, transparent),
            radial-gradient(1px 1px at 50px 50px, #ddd, transparent),
            radial-gradient(1px 1px at 130px 80px, #fff, transparent),
            radial-gradient(2px 2px at 90px 10px, #fff, transparent);
        background-repeat: repeat;
        background-size: 200px 200px;
        animation: stars-twinkle 3s ease-in-out infinite;
        z-index: -1;
        pointer-events: none;
    }
    
    /* Cosmic Header Glow */
    .cosmic-header {
        background: linear-gradient(90deg, #4a148c 0%, #1a237e 50%, #01579b 100%);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 30px rgba(138, 43, 226, 0.5);
        animation: cosmic-pulse 4s ease-in-out infinite;
        text-align: center;
    }
    
    .cosmic-header h1 {
        color: #e1bee7;
        text-shadow: 0 0 20px rgba(186, 104, 200, 0.8);
        margin: 0;
        font-size: 2.5rem;
    }
    
    .cosmic-header p {
        color: #b39ddb;
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
    }
    
    /* Cosmic Sidebar Enhancement */
    .cosmic-sidebar-header {
        background: linear-gradient(135deg, #5e35b1 0%, #311b92 100%);
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        text-align: center;
        box-shadow: 0 0 20px rgba(94, 53, 177, 0.4);
    }
    
    .cosmic-sidebar-header h2 {
        color: #e1bee7;
        margin: 0;
        font-size: 1.5rem;
        text-shadow: 0 0 10px rgba(186, 104, 200, 0.6);
    }
    
    /* Cosmic Navigation Buttons */
    .cosmic-nav-button {
        background: linear-gradient(90deg, #512da8 0%, #311b92 100%);
        color: #e1bee7;
        border: 2px solid #7e57c2;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(126, 87, 194, 0.3);
    }
    
    .cosmic-nav-button:hover {
        background: linear-gradient(90deg, #673ab7 0%, #512da8 100%);
        box-shadow: 0 0 20px rgba(126, 87, 194, 0.6);
        transform: translateY(-2px);
    }
    
    /* Cosmic Metrics Cards */
    .cosmic-metric {
        background: linear-gradient(135deg, #1a237e 0%, #0d47a1 100%);
        border: 1px solid #5c6bc0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #bbdefb;
        box-shadow: 0 0 15px rgba(92, 107, 192, 0.3);
    }
    
    .cosmic-metric h3 {
        color: #e3f2fd;
        margin: 0 0 0.5rem 0;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .cosmic-metric .value {
        color: #fff;
        font-size: 1.8rem;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    
    /* Cosmic Accent Elements */
    .cosmic-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, #7e57c2 50%, transparent 100%);
        margin: 1.5rem 0;
        box-shadow: 0 0 10px rgba(126, 87, 194, 0.5);
    }
    
    /* Nebula Effect for Cards */
    .cosmic-card {
        background: rgba(26, 35, 126, 0.3);
        border: 1px solid rgba(126, 87, 194, 0.4);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 20px rgba(126, 87, 194, 0.2);
    }
    
    /* Stardust Particles */
    .stardust {
        position: fixed;
        width: 3px;
        height: 3px;
        background: white;
        border-radius: 50%;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.8);
        animation: stars-twinkle 2s ease-in-out infinite;
        z-index: -1;
        pointer-events: none;
    }
</style>
"""


def apply_cosmic_theme():
    """
    Apply the cosmic theme CSS to the Streamlit dashboard.
    
    This function injects the cosmic CSS styling into the page
    using Streamlit's markdown with unsafe_allow_html enabled.
    
    Returns:
        bool: True if the theme was successfully applied
    """
    try:
        st.markdown(COSMIC_CSS, unsafe_allow_html=True)
        return True
    except Exception as e:
        st.warning(f"Could not apply cosmic theme: {e}")
        return False

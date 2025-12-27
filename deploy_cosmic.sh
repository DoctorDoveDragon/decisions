#!/bin/bash
# deploy_cosmic.sh - Safe deployment helper for cosmic theme overlay

set -e  # Exit on error

echo "🌌 Cosmic Theme Deployment Script"
echo "=================================="
echo ""

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Create cosmic_upgrade directory if it doesn't exist
echo "📁 Step 1: Ensuring cosmic_upgrade/ directory exists..."
if [ ! -d "cosmic_upgrade" ]; then
    mkdir -p cosmic_upgrade
    echo -e "${GREEN}✓${NC} Created cosmic_upgrade/ directory"
else
    echo -e "${YELLOW}✓${NC} cosmic_upgrade/ directory already exists"
fi

# Step 2: Check/create __init__.py if missing
echo ""
echo "📝 Step 2: Checking cosmic_upgrade/__init__.py..."
if [ ! -f "cosmic_upgrade/__init__.py" ]; then
    cat > cosmic_upgrade/__init__.py << 'EOF'
"""
Cosmic Upgrade - Optional Theme Overlay for Streamlit Dashboard
A non-breaking, drop-in cosmic theme enhancement
"""

__version__ = "1.0.0"
__author__ = "DoctorDoveDragon"
EOF
    echo -e "${GREEN}✓${NC} Created cosmic_upgrade/__init__.py"
else
    echo -e "${YELLOW}✓${NC} cosmic_upgrade/__init__.py already exists"
fi

# Step 3: Check/update requirements.txt for plotly
echo ""
echo "📦 Step 3: Checking requirements.txt for plotly..."
if [ -f "requirements.txt" ]; then
    if grep -q "plotly" requirements.txt; then
        echo -e "${YELLOW}✓${NC} plotly already in requirements.txt"
    else
        echo -e "${YELLOW}!${NC} plotly not found in requirements.txt (already present in mechanical process deps)"
    fi
else
    echo -e "${RED}✗${NC} requirements.txt not found"
fi

# Step 4: Local import test
echo ""
echo "🧪 Step 4: Testing local import (optional - requires streamlit)..."
python3 << 'PYEOF'
import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

# Mock streamlit for testing if not available
try:
    import streamlit
except ImportError:
    # Create a minimal mock for testing
    import types
    streamlit = types.ModuleType('streamlit')
    streamlit.markdown = lambda *args, **kwargs: None
    streamlit.warning = lambda *args, **kwargs: None
    streamlit.sidebar = types.SimpleNamespace()
    sys.modules['streamlit'] = streamlit
    print("! Using mock streamlit for testing (streamlit not installed)")

try:
    # Test import
    from cosmic_upgrade import theme
    print("✓ Successfully imported cosmic_upgrade.theme")
    
    # Check for required functions
    if hasattr(theme, 'apply_cosmic_theme'):
        print("✓ apply_cosmic_theme() function found")
    else:
        print("✗ apply_cosmic_theme() function not found")
        sys.exit(1)
    
    if hasattr(theme, 'COSMIC_CSS'):
        print("✓ COSMIC_CSS string found")
    else:
        print("✗ COSMIC_CSS string not found")
        sys.exit(1)
    
    print("✓ All import tests passed")
    
except ImportError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Test failed: {e}")
    sys.exit(1)
PYEOF

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Local import test passed"
else
    echo -e "${YELLOW}!${NC} Local import test failed (this is OK if streamlit is not installed yet)"
fi

# Step 5: Backup dashboard/app.py if it exists
echo ""
echo "💾 Step 5: Backing up dashboard/app.py..."
if [ -f "dashboard/app.py" ]; then
    BACKUP_FILE="dashboard/app_backup_$(date +%Y%m%d_%H%M%S).py"
    cp dashboard/app.py "$BACKUP_FILE"
    echo -e "${GREEN}✓${NC} Created backup: $BACKUP_FILE"
else
    echo -e "${YELLOW}!${NC} dashboard/app.py not found, skipping backup"
fi

# Step 6: Print integration instructions
echo ""
echo "================================================"
echo -e "${GREEN}✅ Cosmic theme deployment complete!${NC}"
echo "================================================"
echo ""
echo "📝 Integration Instructions:"
echo ""
echo "To activate the cosmic theme, add the following lines to the TOP of dashboard/app.py"
echo "(BEFORE st.set_page_config):"
echo ""
echo "---------------------------------------------------"
cat << 'EOF'
# Cosmic Theme Overlay (optional, non-breaking)
try:
    from cosmic_upgrade.upgrade import upgrade_existing_dashboard
    if upgrade_existing_dashboard():
        import streamlit as st
        st.toast("🌌 Cosmic mode activated!", icon="✨")
except ImportError:
    pass  # Cosmic upgrade not available, continue normally
EOF
echo "---------------------------------------------------"
echo ""
echo "Or copy the integration snippet from:"
echo "  dashboard_cosmic_integration_snippet.py"
echo ""
echo "Then run:"
echo "  streamlit run dashboard/app.py"
echo ""
echo "To verify deployment, you can run:"
echo "  python3 -c 'from cosmic_upgrade.verify import verify_deployment; verify_deployment()'"
echo ""
echo "Or integrate it into a Streamlit page/route."
echo ""

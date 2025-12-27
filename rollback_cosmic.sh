#!/bin/bash
# rollback_cosmic.sh - Rollback helper for cosmic theme overlay

set -e  # Exit on error

echo "🔄 Cosmic Theme Rollback Script"
echo "================================"
echo ""

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Remove cosmic import from dashboard/app.py
echo "🔍 Step 1: Checking dashboard/app.py for cosmic imports..."
if [ -f "dashboard/app.py" ]; then
    # Check if cosmic import exists
    if grep -q "cosmic_upgrade" dashboard/app.py; then
        echo -e "${YELLOW}!${NC} Found cosmic_upgrade imports in dashboard/app.py"
        
        # Create a temporary file without the cosmic block
        echo "Removing cosmic import block..."
        
        # Use sed to remove the cosmic block (try-except block containing cosmic_upgrade)
        # This is a simple approach - remove lines between "# Cosmic Theme" and "except ImportError:"
        python3 << 'PYEOF'
import re

with open('dashboard/app.py', 'r') as f:
    content = f.read()

# Pattern to match the cosmic upgrade block
# Looking for the try-except block with cosmic_upgrade
pattern = r'# Cosmic Theme.*?except ImportError:\s+pass.*?\n'
new_content = re.sub(pattern, '', content, flags=re.DOTALL)

# Also try alternative pattern
pattern2 = r'try:\s+from cosmic_upgrade\.upgrade.*?except.*?pass.*?\n'
new_content = re.sub(pattern2, '', new_content, flags=re.DOTALL)

with open('dashboard/app.py', 'w') as f:
    f.write(new_content)

print("✓ Removed cosmic import block from dashboard/app.py")
PYEOF
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓${NC} Removed cosmic imports from dashboard/app.py"
        else
            echo -e "${RED}✗${NC} Failed to remove cosmic imports automatically"
            echo "Please manually remove the cosmic import block from dashboard/app.py"
        fi
    else
        echo -e "${GREEN}✓${NC} No cosmic imports found in dashboard/app.py"
    fi
else
    echo -e "${YELLOW}!${NC} dashboard/app.py not found"
fi

# Step 2: Prompt to remove cosmic_upgrade directory
echo ""
echo "📁 Step 2: cosmic_upgrade/ directory removal"
if [ -d "cosmic_upgrade" ]; then
    echo -e "${YELLOW}!${NC} cosmic_upgrade/ directory found"
    read -p "Do you want to remove the cosmic_upgrade/ directory? (y/N): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf cosmic_upgrade
        echo -e "${GREEN}✓${NC} Removed cosmic_upgrade/ directory"
    else
        echo -e "${BLUE}→${NC} Keeping cosmic_upgrade/ directory"
    fi
else
    echo -e "${GREEN}✓${NC} cosmic_upgrade/ directory not found"
fi

# Step 3: Restore backup (optional)
echo ""
echo "💾 Step 3: Backup restoration (optional)"

# Find the most recent backup
LATEST_BACKUP=$(ls -t dashboard/app_backup_*.py 2>/dev/null | head -n1)

if [ -n "$LATEST_BACKUP" ]; then
    echo -e "${BLUE}→${NC} Found backup: $LATEST_BACKUP"
    read -p "Do you want to restore this backup? (y/N): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [ -f "dashboard/app.py" ]; then
            # Create a pre-rollback backup
            PREROLLBACK_BACKUP="dashboard/app_pre_rollback_$(date +%Y%m%d_%H%M%S).py"
            cp dashboard/app.py "$PREROLLBACK_BACKUP"
            echo -e "${GREEN}✓${NC} Created pre-rollback backup: $PREROLLBACK_BACKUP"
        fi
        
        # Restore from backup
        cp "$LATEST_BACKUP" dashboard/app.py
        echo -e "${GREEN}✓${NC} Restored dashboard/app.py from $LATEST_BACKUP"
    else
        echo -e "${BLUE}→${NC} Keeping current dashboard/app.py"
    fi
else
    echo -e "${YELLOW}!${NC} No backups found"
fi

# Final status
echo ""
echo "================================================"
echo -e "${GREEN}✅ Cosmic theme rollback complete!${NC}"
echo "================================================"
echo ""
echo "Summary of actions:"
echo "  - Removed cosmic imports from dashboard/app.py (if found)"
if [ -d "cosmic_upgrade" ]; then
    echo "  - cosmic_upgrade/ directory: KEPT (user choice)"
else
    echo "  - cosmic_upgrade/ directory: REMOVED"
fi
echo ""
echo "To complete the rollback:"
echo "  1. Verify dashboard/app.py is correct"
echo "  2. Restart the Streamlit application"
echo "  3. Optionally remove backup files from dashboard/"
echo ""

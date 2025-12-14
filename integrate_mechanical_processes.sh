#!/bin/bash
# ============================================================================
# INTEGRATION SCRIPT: Mechanical Process Framework
# ENTER INTO: Terminal/Bash (run from project directory)
# PURPOSE: Integrate mechanical process framework with existing platform
# ============================================================================

echo -e "${BLUE}🔧 Integrating Mechanical Process Framework...${NC}"

# Update API server imports
echo "Updating API imports..."
if ! grep -q "mechanical_processes" api/server.py; then
    echo "Already integrated"
else
    echo "✓ API already includes mechanical processes"
fi

# Create __init__.py for mechanical processes
cat > core/mechanical_processes/__init__.py << 'INIT_EOF'
"""
Mechanical Process Analysis Module
Version: 1.0.0
"""

from core.mechanical_processes.base_process import (
    BaseMechanicalProcess,
    ProcessAnalysis,
    ProcessCategory,
    ProcessDimension,
    FormulaRepresentation,
    EtymologyAnalysis,
    TheoreticalFoundation,
    CulturalInterpretation,
    UtilityAnalysis
)

from core.mechanical_processes.process_factory import MechanicalProcessFactory
from core.mechanical_processes.entropy_process import EntropyProcess

__all__ = [
    "BaseMechanicalProcess",
    "ProcessAnalysis", 
    "ProcessCategory",
    "ProcessDimension",
    "FormulaRepresentation",
    "EtymologyAnalysis",
    "TheoreticalFoundation",
    "CulturalInterpretation",
    "UtilityAnalysis",
    "MechanicalProcessFactory",
    "EntropyProcess"
]

__version__ = "1.0.0"
INIT_EOF
echo "✓ Created mechanical processes __init__.py"

# Update main __init__.py
cat > core/__init__.py << 'CORE_INIT_EOF'
"""
Comparative Decision Intelligence Core Module
Enterprise Edition
"""

__version__ = "2.0.0"
__author__ = "Comparative Decision Intelligence Team"

# Import both modules
from core.traditions.tradition_factory import TraditionFactory
from core.comparative_engine import ComparativeEngine
from core.mechanical_processes.process_factory import MechanicalProcessFactory

__all__ = [
    "TraditionFactory",
    "ComparativeEngine", 
    "MechanicalProcessFactory"
]

def get_modules():
    """Get available analysis modules"""
    return {
        "philosophical_analysis": {
            "module": "core.traditions",
            "version": "1.0.0",
            "description": "Philosophical tradition analyzers"
        },
        "mechanical_processes": {
            "module": "core.mechanical_processes", 
            "version": "1.0.0",
            "description": "Mechanical process analysis through 5 dimensions"
        }
    }
CORE_INIT_EOF
echo "✓ Updated core __init__.py"

# Create example analysis script
cat > examples/mechanical_process_example.py << 'EXAMPLE_EOF'
#!/usr/bin/env python3
"""
Example: Mechanical Process Analysis
"""

import sys
sys.path.append('.')

from core.mechanical_processes.process_factory import MechanicalProcessFactory

def main():
    print("🔧 Mechanical Process Analysis Example")
    print("=" * 50)
    
    factory = MechanicalProcessFactory()
    
    # 1. List available processes
    print("\n1. Available Processes:")
    processes = factory.get_all_processes()
    for name, info in processes.items():
        print(f"   • {name}: {info['description']}")
    
    # 2. Analyze entropy
    print("\n2. Analyzing Entropy Process:")
    analysis = factory.analyze_process("entropy")
    
    print(f"   Category: {analysis['result']['category']}")
    print(f"   Formula: {analysis['result']['formula']['symbolic']}")
    
    # 3. Show dimensional profile
    print("\n3. Dimensional Profile:")
    profile = analysis['result']['dimensional_profile']
    for dimension, score in profile.items():
        bars = "█" * int(score * 10)
        print(f"   {dimension:12} {bars:10} {score:.2f}")
    
    # 4. Show insights
    print("\n4. Key Insights:")
    for i, insight in enumerate(analysis['result']['synthesis'][:3], 1):
        print(f"   {i}. {insight}")
    
    print("\n✅ Example complete!")
    print("\nNext: Try the API at http://localhost:8000/api/v1/mechanical-processes")
    print("Or use the dashboard at http://localhost:8501")

if __name__ == "__main__":
    main()
EXAMPLE_EOF

chmod +x examples/mechanical_process_example.py
echo "✓ Created example script"

# Create examples directory if not exists
mkdir -p examples

echo ""
echo -e "${GREEN}✅ Mechanical Process Framework Integrated!${NC}"
echo ""
echo -e "${BLUE}New Features Added:${NC}"
echo "1. 🔧 Base mechanical process class with 5-dimensional analysis"
echo "2. 📐 Entropy process analyzer (formula, etymology, theory, culture, utility)"
echo "3. 🏭 Process factory for creating/managing process analyzers"
echo "4. 🌐 API endpoints at /api/v1/mechanical-processes/"
echo "5. 📊 Dashboard page for interactive process analysis"
echo "6. 📈 Dimensional visualization with Plotly"
echo ""
echo -e "${BLUE}To test:${NC}"
echo "1. Install new dependencies:"
echo "   ${GREEN}pip install sympy plotly pandas networkx${NC}"
echo "2. Start platform:"
echo "   ${GREEN}./start.sh${NC}"
echo "3. Open dashboard:"
echo "   ${GREEN}http://localhost:8501${NC}"
echo "4. Navigate to: '🔧 Mechanical Processes'"
echo ""
echo -e "${YELLOW}Or run example:${NC}"
echo "   ${GREEN}python examples/mechanical_process_example.py${NC}"

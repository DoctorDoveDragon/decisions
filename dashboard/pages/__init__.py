# dashboard/__init__.py
"""
Comparative Decision Intelligence Dashboard Module
"""

__version__ = "1.0.0"
__author__ = "Comparative Decision Intelligence Team"

# dashboard/pages/__init__.py
"""
Dashboard Pages Module
"""

# Note: We don't import mechanical_processes here to avoid loading its heavy dependencies
# It will be imported on-demand when needed
from . import home
from . import analysis

__all__ = ["home", "analysis"]

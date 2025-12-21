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

from . import home
from . import analysis
from . import mechanical_processes

__all__ = ["home", "analysis", "mechanical_processes"]

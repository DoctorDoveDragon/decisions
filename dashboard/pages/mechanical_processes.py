"""
Mechanical Processes page - wrapper for the emoji-named file.
"""

# Import from the emoji-named file
from importlib import import_module

# Import the actual module
_emoji_module = import_module("dashboard.pages.3_🧠_Mechanical_Processes")

# Re-export the main function
main = _emoji_module.main

__all__ = ["main"]

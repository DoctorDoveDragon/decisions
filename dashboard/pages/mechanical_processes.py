"""
Mechanical Processes Page Module (Canonical Wrapper)

This module provides the canonical import path for the mechanical processes page.
It loads the actual implementation from 3_🧠_Mechanical_Processes.py and exposes the main() function.
"""

import os
from importlib.machinery import SourceFileLoader

# Get the directory containing this file
_current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the actual implementation from the emoji-named file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")
_loader = SourceFileLoader("_mechanical_processes_impl", _original_file)
_impl = _loader.load_module()

# Expose the main function from the loaded module
main = _impl.main

# Expose any other public functions or attributes if needed
__all__ = ["main"]

"""
Mechanical Processes Page Module

This module provides a canonical import path for the mechanical processes page.
It loads the original file (3_🧠_Mechanical_Processes.py) and exposes its main() function.
"""

import os
import sys
from importlib.machinery import SourceFileLoader

# Get the directory containing this file
_current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the original mechanical processes file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")

# Load the original module using SourceFileLoader
_loader = SourceFileLoader("_mechanical_processes_impl", _original_file)
_mechanical_processes_module = _loader.load_module()

# Expose the main() function from the original module
def main():
    """
    Render the Mechanical Processes page.
    This function delegates to the main() function in the original file.
    """
    return _mechanical_processes_module.main()

# Expose other commonly used functions if needed
__all__ = ["main"]

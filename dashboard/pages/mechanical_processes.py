"""
Mechanical Processes Page Module

This module provides a canonical import path for the mechanical processes page.
It loads the original file (3_🧠_Mechanical_Processes.py) and exposes its main() function.
"""

import os
import importlib.util
import sys

# Get the directory containing this file
_current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the original mechanical processes file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")

# Load the original module using modern importlib API
try:
    if not os.path.exists(_original_file):
        raise FileNotFoundError(
            f"Original mechanical processes file not found: {_original_file}"
        )
    
    _spec = importlib.util.spec_from_file_location("_mechanical_processes_impl", _original_file)
    if _spec is None or _spec.loader is None:
        raise ImportError(
            f"Failed to create module spec for: {_original_file}"
        )
    
    _impl_module = importlib.util.module_from_spec(_spec)
    sys.modules[_spec.name] = _impl_module
    _spec.loader.exec_module(_impl_module)
    
except (FileNotFoundError, ImportError) as e:
    raise ImportError(
        f"Failed to load mechanical processes module: {e}"
    ) from e

# Expose the main() function from the original module
def main():
    """
    Render the Mechanical Processes page.
    This function delegates to the main() function in the original file.
    """
    return _impl_module.main()

__all__ = ["main"]

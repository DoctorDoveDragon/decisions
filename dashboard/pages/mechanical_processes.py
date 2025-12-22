"""
Mechanical Processes Page Module (Canonical Wrapper)

This module provides the canonical import path for the mechanical processes page.
It loads the actual implementation from 3_🧠_Mechanical_Processes.py and exposes the main() function.
"""

import os
import importlib.util

# Get the directory containing this file
_current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the actual implementation from the emoji-named file
_original_file = os.path.join(_current_dir, "3_🧠_Mechanical_Processes.py")

try:
    # Use modern importlib approach (Python 3.4+)
    _spec = importlib.util.spec_from_file_location("_mechanical_processes_impl", _original_file)
    if _spec is None:
        raise ImportError(f"Cannot create module spec from {_original_file}")
    
    _impl = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_impl)
    
    # Expose the main function from the loaded module
    if not hasattr(_impl, 'main'):
        raise AttributeError(f"Module {_original_file} does not have a main() function")
    
    main = _impl.main
except (ImportError, AttributeError, FileNotFoundError) as e:
    raise ImportError(
        f"Failed to load mechanical processes implementation from {_original_file}: {e}"
    ) from e

# Expose any other public functions or attributes if needed
__all__ = ["main"]

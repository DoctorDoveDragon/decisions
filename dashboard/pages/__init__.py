"""
dashboard.pages package initializer

Keep this file minimal to avoid import-time side effects and circular imports.
Do NOT import submodules here; import them lazily where needed.
"""

__all__ = ["home", "analysis", "mechanical_processes"]
__version__ = "0.1.0"

import importlib
from types import ModuleType
from typing import Any

# Known page names we expect in this package
_PAGE_NAMES = set(__all__)

def _load_page_module(name: str) -> ModuleType:
    """Import and cache a page module by name."""
    if name not in _PAGE_NAMES:
        raise AttributeError(f"module 'dashboard.pages' has no attribute '{name}'")
    # Check if already cached
    if name in globals():
        return globals()[name]
    module = importlib.import_module(f"dashboard.pages.{name}")
    globals()[name] = module  # cache for future attribute access
    return module

def __getattr__(name: str) -> Any:
    """Lazy-load page modules as attributes (PEP 562)."""
    if name in _PAGE_NAMES:
        return _load_page_module(name)
    raise AttributeError(f"module 'dashboard.pages' has no attribute '{name}'")

def __dir__() -> list:
    """Expose the expected attributes in completion."""
    return sorted(list(globals().keys()) + list(_PAGE_NAMES))

def get_page(name: str) -> ModuleType:
    """Programmatic helper to import a page module."""
    return _load_page_module(name)

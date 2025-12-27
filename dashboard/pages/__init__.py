# dashboard/pages/__init__.py
"""
Dashboard Pages Module
"""

# Do NOT import page submodules at package-import time — that can cause circular imports.
# Provide lazy-loading of the commonly used page modules instead.

__all__ = ["home", "analysis", "mechanical_processes"]

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

__all__ = ["home", "analysis", "mechanical_processes"]

import importlib
from types import ModuleType
from typing import Any

# Known page names we expect in this package
_PAGE_NAMES = set(__all__)

def _load_page_module(name: str) -> ModuleType:
    """Import and cache a page module by name."""
    if name not in _PAGE_NAMES:
        raise AttributeError(f"module 'dashboard.pages' has no attribute '{name}'")
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
# Note: We don't import mechanical_processes here to avoid loading its heavy dependencies
# It will be imported on-demand when needed
from . import home
from . import analysis

__all__ = ["home", "analysis"]

"""
dashboard.pages package initializer

Keep this file minimal to avoid import-time side effects and circular imports.
Do NOT import submodules here; import them lazily where needed.
"""

__all__ = [
    # List available page module names (strings) for reference.
    # Do NOT import the actual modules here to avoid circular imports.
    "home",
    "analysis",
    "mechanical_processes",
    "philosophical_analysis",
    # Note: "3_🧠_Mechanical_Processes" is the actual filename but cannot be imported directly.
    # Use "mechanical_processes" which wraps it for canonical imports.
]
__version__ = "0.1.0"

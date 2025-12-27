"""
Launcher for the decisions dashboard.
"""
import sys
import os


def launch():
    """Launch the decisions dashboard using streamlit."""
    # When called as a console script, this will launch streamlit
    # pointing to the installed package's app.py
    import subprocess
    
    # Get the path to app.py in the installed package
    import decisions.dashboard.app as app_module
    app_path = app_module.__file__
    
    # Launch streamlit with the app
    cmd = ['streamlit', 'run', app_path] + sys.argv[1:]
    return subprocess.call(cmd)


if __name__ == '__main__':
    sys.exit(launch())

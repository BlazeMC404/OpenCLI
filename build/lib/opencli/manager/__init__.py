"""
OpenCLI Manager Package

This package provides all core management logic for OpenCLI operations,
including terminal setup, command handling, and shell initialization.
"""

import logging

from opencli.config import logger as opencli_logger

# Import core managers
from .setup_manager import setup_terminal, _copy_shell_template
from .command_manager import add_existing_command, create_new_command

# Optionally expose managers in __all__
__all__ = [
    "setup_terminal",
    "add_existing_command",
    "create_new_command",
    "_copy_shell_template"
]

# Log manager init
opencli_logger.debug("OpenCLI Manager package initialized successfully.")

# Optional: Plugin discovery or dynamic extensions could be registered here
def initialize_plugins():
    # Placeholder for future plugin system
    opencli_logger.debug("Plugin initialization stub called (not implemented).")

initialize_plugins()
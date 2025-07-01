"""
OpenCLI - Python Terminal Creation Framework

OpenCLI is a powerful framework for creating Python-based command-line terminals
with customizable command sets and shells.

Author: BlazeMC404
License: MIT
Repository: https://github.com/BlazeMC404/OpenCLI
"""

import logging

# Version
__version__ = "1.0.1"
__author__ = "BlazeMC404"
__license__ = "MIT"

# Logging setup
from opencli.config import logger as opencli_logger
opencli_logger.debug("OpenCLI core package initialized.")

# Import public interfaces from manager
from opencli.manager.setup_manager import setup_terminal as setup
from opencli.manager.command_manager import (
    add_existing_command as addcmd,
    create_new_command as newcmd,
)

# Colors for terminal
from opencli.manager.color_manager import Colors as colors

# Shell interface (optional helper)
from opencli.manager.shell_launcher import run_shell as shell

# Public API (for from opencli import *)
__all__ = [
    "__version__",
    "setup",
    "addcmd",
    "newcmd",
    "shell",
    "colors"
]
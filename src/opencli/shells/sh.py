#!/usr/bin/env python3
"""
Auto-generated sh shell launcher.
This file was created by the OpenCLI setup utility.

Author: OpenCLI System
Shell Type: sh
"""

import sys
import argparse
from pathlib import Path

from opencli.shells.shell_launcher import run_shell
from opencli.config import Colors, logger

def parse_args():
    parser = argparse.ArgumentParser(
        description="Launch the OpenCLI sh shell"
    )
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug logging"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Enable debug logging if --debug is passed
    if args.debug:
        import logging
        logger.setLevel(logging.DEBUG)
        logger.debug(f"{Colors.BRIGHT_YELLOW}[DEBUG MODE ENABLED]{Colors.RESET}")

    # Detect terminal name from path
    terminal_path = Path(__file__).resolve().parent
    terminal_name = terminal_path.name

    print(f"{Colors.BRIGHT_MAGENTA}Launching OpenCLI sh shell for terminal: '{terminal_name}'...{Colors.RESET}")
    
    try:
        run_shell(terminal_name=terminal_name, shell_name="sh")
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_RED}Shell interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(130)
    except Exception as e:
        logger.critical(f"{Colors.FAIL}Unexpected error: {e}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
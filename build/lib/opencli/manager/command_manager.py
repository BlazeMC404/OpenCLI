import os
from pathlib import Path
from typing import Optional

from opencli.config import logger, Colors, config


TEMPLATE_COMMANDS = {
    "ls": "ls",
    "clear": "clear",
    "cat": "cat",
    "echo": "echo",
    "pwd": "pwd",
    "mkdir": "mkdir",
    "rm": "rm",
    "touch": "touch"
}

TEMPLATE_IMPORT_LINE = "from opencli.templates import {template}"


def _validate_terminal(terminal_name: str):
    terminal_path = Path.cwd() / terminal_name
    if not terminal_path.exists() or not (terminal_path / "bin").exists():
        logger.error(f"{Colors.FAIL}Terminal '{terminal_name}' does not exist or is improperly set up.{Colors.RESET}")
        raise FileNotFoundError(f"Invalid terminal: {terminal_name}")
    return terminal_path


def _write_command_file(bin_path: Path, name: str, content: str):
    command_file = bin_path / f"{name}.py"
    if command_file.exists():
        logger.warning(f"{Colors.YELLOW}Command '{name}' already exists. Overwriting...{Colors.RESET}")
    with open(command_file, "w") as f:
        f.write(content)
    logger.info(f"{Colors.BRIGHT_GREEN}Command created: {command_file.name}{Colors.RESET}")


def addcmd(terminal_name: str, command_name: str):
    """
    Adds a prebuilt command template to the terminal/bin directory.
    """
    logger.debug(f"Attempting to add template command: {command_name} to terminal: {terminal_name}")
    if command_name not in TEMPLATE_COMMANDS:
        logger.error(f"{Colors.FAIL}Unknown command template: '{command_name}'{Colors.RESET}")
        raise ValueError(f"Unknown command: {command_name}")

    terminal_path = _validate_terminal(terminal_name)
    bin_path = terminal_path / "bin"
    template_module = TEMPLATE_COMMANDS[command_name]

    code = f'''"""
Auto-generated template command: {command_name}
"""

{TEMPLATE_IMPORT_LINE.format(template=template_module)}

def main():
    {template_module}.{command_name}()

if __name__ == "__main__":
    main()
'''

    _write_command_file(bin_path, command_name, code)


def newcmd(terminal_name: str, command_name: str, command_code: str, author: Optional[str] = None, description: Optional[str] = None):
    """
    Creates a fully custom command with provided Python code.
    """
    logger.debug(f"Creating custom command: {command_name} in terminal: {terminal_name}")
    terminal_path = _validate_terminal(terminal_name)
    bin_path = terminal_path / "bin"

    metadata = f"# Author: {author or 'unknown'}\n# Description: {description or 'No description'}"
    full_code = f'''"""
Custom OpenCLI command: {command_name}
"""

{metadata}

def main():
{_indent_code(command_code)}

if __name__ == "__main__":
    main()
'''

    _write_command_file(bin_path, command_name, full_code)


def _indent_code(code: str, indent: int = 4) -> str:
    """
    Indents multi-line code for embedding into a Python function.
    """
    indentation = " " * indent
    return "\n".join(f"{indentation}{line}" if line.strip() else "" for line in code.splitlines())
    
import os
import shutil
import logging

logger = logging.getLogger("opencli")

import shutil
import logging
from pathlib import Path

logger = logging.getLogger("opencli")

def add_existing_command(terminal_name: str, command_name: str) -> None:
    """
    Copy an existing command template from opencli/src/opencli/commands
    into the terminal's bin directory.
    """
    current_dir = Path(__file__).parent
    commands_dir = current_dir.parent / "commands"
    bin_dir = Path.cwd() / terminal_name / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)

    template_path = commands_dir / f"{command_name}.py"
    target_path = bin_dir / f"{command_name}.py"

    if not template_path.is_file():
        logger.error(f"Command template '{command_name}.py' not found in '{commands_dir}'.")
        raise FileNotFoundError(f"Command template '{command_name}.py' not found.")

    shutil.copy(template_path, target_path)
    logger.info(f"Copied command '{command_name}' to terminal '{terminal_name}'.")
        
def create_new_command(terminal_name: str, command_name: str, code: str) -> None:
    """
    Creates a new command file with the given code inside the terminal's bin directory.

    Args:
        terminal_name (str): Name of the terminal.
        command_name (str): Name of the new command.
        code (str): Python code to include in the command.
    """
    import os

    bin_dir = os.path.join(os.getcwd(), terminal_name, "bin")
    os.makedirs(bin_dir, exist_ok=True)

    filepath = os.path.join(bin_dir, f"{command_name}.py")
    with open(filepath, "w") as f:
        f.write(code)        
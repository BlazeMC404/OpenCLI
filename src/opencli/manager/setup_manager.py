import os
import sys
from pathlib import Path
from opencli.config import logger, Colors, config

SUPPORTED_SHELLS = {
    "opencli": "opencli_shell",
    "bash": "bash_shell",
    "sh": "sh_shell"
}

SHELL_HEADER = '''"""
Auto-generated shell entrypoint for {shell_type} shell.
Do not modify unless you know what you're doing.
"""'''


def _validate_shell(shell_type: str):
    if shell_type not in SUPPORTED_SHELLS:
        logger.error(f"{Colors.FAIL}Unsupported shell: '{shell_type}'. Supported shells are: {list(SUPPORTED_SHELLS.keys())}{Colors.RESET}")
        raise ValueError(f"Invalid shell: {shell_type}")


def _create_shell_script(terminal_dir: Path, shell_type: str):
    shell_file = terminal_dir / f"{shell_type}.py"
    shell_module = SUPPORTED_SHELLS[shell_type]

    content = f"""{SHELL_HEADER.format(shell_type=shell_type)}

from opencli.shells import {shell_module}
from opencli.templates import echo_template

# Add default command bindings
commands = {{
    "echo": echo_template.echo
}}

if __name__ == "__main__":
    {shell_module}.run(commands)
"""

    with open(shell_file, 'w') as f:
        f.write(content)

    logger.info(f"{Colors.BRIGHT_GREEN}Shell script created: {shell_file.name}{Colors.RESET}")


def _create_directory_structure(base_path: Path):
    try:
        (base_path / "bin").mkdir(parents=True, exist_ok=True)
        logger.info(f"{Colors.BRIGHT_BLUE}Created: {base_path / 'bin'}{Colors.RESET}")
    except Exception as e:
        logger.error(f"{Colors.FAIL}Failed to create directory structure: {e}{Colors.RESET}")
        raise


def setup_terminal(terminal_name: str, shell_type: str = "opencli"):
    """
    Sets up a new terminal environment with shell and bin/ directory.

    :param terminal_name: Name of the terminal to be created.
    :param shell_type: One of ['opencli', 'bash', 'sh']
    """
    logger.debug(f"Initializing setup for terminal: {terminal_name} with shell: {shell_type}")
    _validate_shell(shell_type)

    terminal_path = Path.cwd() / terminal_name

    if terminal_path.exists():
        logger.warning(f"{Colors.YELLOW}Terminal directory '{terminal_name}' already exists. Setup aborted.{Colors.RESET}")
        return

    try:
        _create_directory_structure(terminal_path)
        _create_shell_script(terminal_path, shell_type)

        # Optionally, add README or initial info
        with open(terminal_path / "README.md", 'w') as f:
            f.write(f"# {terminal_name}\nGenerated with OpenCLI using `{shell_type}` shell.\n")

        logger.info(f"{Colors.GREEN}Terminal setup complete for '{terminal_name}' with shell '{shell_type}'.{Colors.RESET}")
    except Exception as e:
        logger.critical(f"{Colors.FAIL}Fatal error during terminal setup: {e}{Colors.RESET}")
        sys.exit(1)
        
import shutil
from pathlib import Path

def _copy_shell_template(terminal_path: Path, shell_name: str):
    templates_dir = Path(__file__).parent / "shells" / "templates"
    template_file = templates_dir / f"{shell_name}.py"

    if not template_file.exists():
        raise ValueError(f"Shell template '{shell_name}' does not exist.")

    dest_file = terminal_path / f"{shell_name}.py"
    shutil.copy(template_file, dest_file)        
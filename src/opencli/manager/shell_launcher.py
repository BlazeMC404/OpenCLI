import os
import sys
import traceback
from pathlib import Path
from importlib import import_module

from opencli.config import logger, Colors


def _get_terminal_banner(shell_name: str):
    return f"{Colors.BRIGHT_CYAN}Welcome to {shell_name} shell powered by OpenCLI!{Colors.RESET}"


def _load_commands(terminal_path: Path):
    commands = {}
    bin_dir = terminal_path / "bin"
    if not bin_dir.exists():
        logger.error(f"{Colors.FAIL}Missing bin/ directory in terminal.{Colors.RESET}")
        return commands

    for file in bin_dir.glob("*.py"):
        command_name = file.stem
        try:
            module_path = f"{terminal_path.name}.bin.{command_name}".replace(os.sep, ".")
            spec = import_module(module_path)
            if hasattr(spec, "main"):
                commands[command_name] = spec.main
                logger.debug(f"Loaded command: {command_name}")
            else:
                logger.warning(f"{Colors.YELLOW}Command '{command_name}' has no 'main()' function.{Colors.RESET}")
        except Exception as e:
            logger.error(f"{Colors.FAIL}Failed to load command '{command_name}': {e}{Colors.RESET}")
    return commands


import shlex
import subprocess
from pathlib import Path

import os
import shlex
import subprocess
from pathlib import Path

def run_shell(terminal_name: str, shell_name: str = "opencli"):
    terminal_path = Path.cwd() / terminal_name
    bin_dir = terminal_path / "bin"

    if not terminal_path.exists():
        logger.critical(f"{Colors.FAIL}Terminal '{terminal_name}' not found.{Colors.RESET}")
        sys.exit(1)

    logger.info(f"Launching {shell_name} shell in terminal '{terminal_name}'")
    print(_get_terminal_banner(shell_name))

    prompt_color = Colors.BRIGHT_GREEN if shell_name == "opencli" else (
        Colors.YELLOW if shell_name == "bash" else Colors.MAGENTA
    )

    try:
        while True:
            try:
                cwd = os.getcwd()
                user_input = input(f"{prompt_color}{terminal_name}@{shell_name}:~$ {Colors.RESET}").strip()
                if not user_input:
                    continue
                if user_input in ("exit", "quit"):
                    print(Colors.BRIGHT_BLUE + "Exiting shell..." + Colors.RESET)
                    break

                parts = shlex.split(user_input)
                command = parts[0]
                args = parts[1:]

                # ✅ Built-in 'cd'
                if command == "cd":
                    if not args:
                        print("No directory provided.")
                    else:
                        try:
                            os.chdir(args[0])
                            print(f"Changed directory to {os.getcwd()}")
                        except Exception as e:
                            print(f"{Colors.FAIL}cd: {e}{Colors.RESET}")
                    continue  # Skip subprocess execution

                cmd_path = bin_dir / f"{command}.py"
                if not cmd_path.exists():
                    print(f"{Colors.RED}Unknown command: '{command}'{Colors.RESET}")
                    continue

                logger.info(f"Executing command: {command} with args: {args}")
                subprocess.run(["python3", str(cmd_path), *args])

            except KeyboardInterrupt:
                print(f"\n{Colors.BRIGHT_YELLOW}^C received. Type 'exit' to quit.{Colors.RESET}")
            except Exception as e:
                logger.error(f"Error in command execution: {e}")
                traceback.print_exc()

    except Exception as shell_error:
        logger.critical(f"{Colors.FAIL}Fatal shell error: {shell_error}{Colors.RESET}")
        sys.exit(1)
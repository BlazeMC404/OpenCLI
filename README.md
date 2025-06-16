# OpenCLI

**OpenCLI** is a Python framework for creating custom terminal environments and command-line shells with ease. It's open source and dependency-free.

---

## Features
- `.setup(terminal_name, shell='opencli')` – Initialize a new terminal folder with chosen shell.
- `.addcmd(command_name)` – Import built-in command templates into your terminal’s `bin` directory.
- `.newcmd(name, code)` – Define and add custom commands dynamically.
- `.shell(shell_name)` – Launch your terminal with the selected shell (`opencli`, `bash`, or `sh`).
- ANSI-colored prompts and outputs.
- Full logging and debug support.
- Extensible architecture with templates and plugins.

---

## Installation

```bash
pip install opencli (coming soon)
```

Or install from source:

```bash
git clone https://github.com/BlazeMC404/OpenCLI.git
cd OpenCLI/dist
pip install opencli-1.0.0-py3-none-any.whl
```

---

## Quickstart

```python
from opencli import setup, addcmd, newcmd, shell

# 1. Setup a new terminal named 'myterminal' with the default 'opencli' shell
setup("myterminal", "opencli")

# 2. Add built-in commands (e.g., echo, ls)
addcmd("myterminal", "echo")
addcmd("myterminal", "ls")

# 3. Create a custom command
custom_code = '''
def run():
    print("Hello from OpenCLI!")
    
'''
newcmd("myterminal", "hello", custom_code)

# 4. Launch the shell
shell("myterminal", shell_name="opencli")
```

---

## Available Shells

- `opencli` - OpenCLI's own shell
- `bash` - Simulated BASH shell
- `sh` - Simulated sh shell

---

## Available Command Templates

- `ls` – Lists directory contents
- `clear` – Clear the terminal screen
- `cd` – Changes the current directory (built-in)
- `cat` – Prints file contents
- `pwd` – Shows current directory
- `mkdir` – Creates a new directory
- `rm` – Removes a file or directory
- `touch` – Creates a new file
- `echo` – Prints text to terminal

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

Make sure your code passes `flake8` and includes appropriate logging.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Note

This project is still in development. You may encounter some issues. Report them in [Issue](https://www.github.com/BlazeMC404/OpenCLI/issue)

---

## Acknowledgements

Thanks to the Linux community and Python ecosystem for inspiring this project.


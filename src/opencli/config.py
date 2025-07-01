import logging
import logging.handlers
import os
import platform
import getpass
import sys
import datetime


# ========== ANSI Color Styling ==========
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    FAIL = '\033[91m'

    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{Colors.RESET}"

    @staticmethod
    def style_log(level, message):
        color_map = {
            "DEBUG": Colors.BRIGHT_CYAN,
            "INFO": Colors.BRIGHT_GREEN,
            "WARNING": Colors.BRIGHT_YELLOW,
            "ERROR": Colors.BRIGHT_RED,
            "CRITICAL": Colors.BOLD + Colors.RED
        }
        return f"{color_map.get(level, Colors.WHITE)}[{level}]{Colors.RESET} {message}"


# ========== Global Configuration ==========
class OpenCLIConfig:
    def __init__(self):
        self.version = "0.1.0"
        self.debug = os.getenv("OPENCLI_DEBUG", "0") == "1"
        self.terminal_width = self._get_terminal_width()
        self.default_shell = "opencli"
        self.author = "BlazeMC"
        self.root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.log_path = os.path.join(self.root_path, "opencli.log")
        self.env = self._gather_env_info()

    def _get_terminal_width(self):
        try:
            import shutil
            return shutil.get_terminal_size().columns
        except:
            return 80

    def _gather_env_info(self):
        return {
            "platform": platform.system(),
            "platform_version": platform.version(),
            "python_version": sys.version,
            "user": getpass.getuser(),
            "cwd": os.getcwd(),
            "time": datetime.datetime.now().isoformat()
        }

    def print_banner(self):
        banner = f"""
{Colors.colorize('┌' + '─' * (self.terminal_width - 2) + '┐', Colors.BRIGHT_BLUE)}
{Colors.colorize('│' + f"{'OpenCLI Terminal Framework'.center(self.terminal_width - 2)}" + '│', Colors.BRIGHT_CYAN)}
{Colors.colorize('│' + f"v{self.version} by {self.author}".center(self.terminal_width - 2) + '│', Colors.BRIGHT_MAGENTA)}
{Colors.colorize('└' + '─' * (self.terminal_width - 2) + '┘', Colors.BRIGHT_BLUE)}
"""
        print(banner)

    def print_env_info(self):
        print(Colors.BOLD + Colors.YELLOW + "Environment Information:" + Colors.RESET)
        for k, v in self.env.items():
            print(f"{Colors.CYAN}{k:>20}{Colors.RESET}: {v}")


# ========== Logging Setup ==========
class OpenCLILogger:
    def __init__(self, config: OpenCLIConfig):
        self.logger = logging.getLogger("OpenCLI")
        self.logger.setLevel(logging.DEBUG if config.debug else logging.INFO)

        formatter = logging.Formatter(
            f"%(asctime)s {Colors.style_log('%(levelname)s', '%(message)s')}",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColoredFormatter())
        self.logger.addHandler(console_handler)

        # Rotating file handler
        file_handler = logging.handlers.RotatingFileHandler(
            config.log_path,
            maxBytes=1024 * 1024,  # 1MB
            backupCount=3
        )
        file_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
        self.logger.addHandler(file_handler)


# ========== Colored Formatter for Console ==========
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        color_map = {
            logging.DEBUG: Colors.BRIGHT_CYAN,
            logging.INFO: Colors.BRIGHT_GREEN,
            logging.WARNING: Colors.BRIGHT_YELLOW,
            logging.ERROR: Colors.BRIGHT_RED,
            logging.CRITICAL: Colors.BOLD + Colors.RED,
        }
        level_color = color_map.get(record.levelno, Colors.WHITE)
        levelname = f"{level_color}[{record.levelname}]{Colors.RESET}"
        formatted = f"{levelname} {record.getMessage()}"
        return formatted


# ========== Initialize Config and Logger ==========
config = OpenCLIConfig()
logger = OpenCLILogger(config).logger
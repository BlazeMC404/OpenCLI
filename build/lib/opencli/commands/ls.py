"""
List directory contents, similar to Unix `ls`.
"""
import os
import argparse
from pathlib import Path
from opencli.config import logger, Colors

def main():
    parser = argparse.ArgumentParser(description="List directory contents")
    parser.add_argument('path', nargs='?', default='.', help="Directory to list")
    parser.add_argument('-a', '--all', action='store_true', help="Include hidden files")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(Colors.FAIL + f"ls: cannot access '{args.path}': No such file or directory" + Colors.RESET)
        return

    entries = sorted(target.iterdir())
    for entry in entries:
        if not args.all and entry.name.startswith('.'):
            continue
        print(entry.name)

if __name__ == '__main__':
    main()
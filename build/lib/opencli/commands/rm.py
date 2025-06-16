#!/usr/bin/env python3
import argparse
import os
import shutil
import sys

def main():
    parser = argparse.ArgumentParser(description="Remove a file or directory")
    parser.add_argument("target", type=str, help="File or directory to remove")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively delete directories")
    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"\033[91mError: '{args.target}' does not exist.\033[0m")
        return

    try:
        if os.path.isfile(args.target):
            os.remove(args.target)
            print(f"\033[92mFile removed: {args.target}\033[0m")
        elif os.path.isdir(args.target):
            if args.recursive:
                shutil.rmtree(args.target)
                print(f"\033[92mDirectory recursively removed: {args.target}\033[0m")
            else:
                print(f"\033[93m'{args.target}' is a directory. Use -r to remove it.\033[0m")
        else:
            print(f"\033[91mError: Unknown file type: {args.target}\033[0m")
    except PermissionError:
        print(f"\033[91mError: Permission denied: {args.target}\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

if __name__ == "__main__":
    main()
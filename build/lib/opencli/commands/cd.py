#!/usr/bin/env python3
"""
Change working directory, similar to Unix `cd`.
"""
import os
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Change the current directory")
    parser.add_argument("directory", type=str, nargs='?', default=None, help="Target directory to change to")
    args = parser.parse_args()

    if args.directory:
        try:
            os.chdir(args.directory)
            print(f"\033[92mChanged directory to {os.getcwd()}\033[0m")
        except FileNotFoundError:
            print(f"\033[91mDirectory not found: {args.directory}\033[0m")
        except PermissionError:
            print(f"\033[91mPermission denied: {args.directory}\033[0m")
        except Exception as e:
            print(f"\033[91mError: {str(e)}\033[0m")
    else:
        print(f"\033[93mNo directory provided.\033[0m")

if __name__ == "__main__":
    main()
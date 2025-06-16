#!/usr/bin/env python3
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Create a new directory")
    parser.add_argument("dirname", type=str, help="Name of the directory to create")
    args = parser.parse_args()

    try:
        os.makedirs(args.dirname, exist_ok=False)
        print(f"\033[92mDirectory created: {args.dirname}\033[0m")
    except FileExistsError:
        print(f"\033[93mWarning: Directory '{args.dirname}' already exists.\033[0m")
    except PermissionError:
        print(f"\033[91mError: Permission denied to create '{args.dirname}'.\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

if __name__ == "__main__":
    main()
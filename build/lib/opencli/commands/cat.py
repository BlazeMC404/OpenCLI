#!/usr/bin/env python3
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Display contents of a file")
    parser.add_argument("filename", type=str, help="Name of the file to read")
    args = parser.parse_args()

    try:
        with open(args.filename, "r") as f:
            content = f.read()
            print(f"\033[96m{content}\033[0m")
    except FileNotFoundError:
        print(f"\033[91mError: File '{args.filename}' not found.\033[0m")
    except PermissionError:
        print(f"\033[91mError: Permission denied to read '{args.filename}'.\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

if __name__ == "__main__":
    main()
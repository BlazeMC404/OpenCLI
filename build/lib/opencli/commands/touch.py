#!/usr/bin/env python3
import argparse
import os
import sys
import time

def main():
    parser = argparse.ArgumentParser(description="Create a file or update its modification time")
    parser.add_argument("filename", type=str, help="Name of the file to touch")
    args = parser.parse_args()

    try:
        if os.path.exists(args.filename):
            # Update timestamp if file exists
            os.utime(args.filename, None)
            print(f"\033[94mTimestamp updated: {args.filename}\033[0m")
        else:
            # Create the file if it doesn't exist
            with open(args.filename, 'a'):
                os.utime(args.filename, None)
            print(f"\033[92mFile created: {args.filename}\033[0m")
    except PermissionError:
        print(f"\033[91mError: Permission denied for '{args.filename}'.\033[0m")
    except Exception as e:
        print(f"\033[91mError: {str(e)}\033[0m")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Echo the input text")
    parser.add_argument("text", nargs='*', help="Text to echo")
    parser.add_argument("-n", action="store_true", help="Do not output the trailing newline")
    parser.add_argument("-e", action="store_true", help="Enable interpretation of backslash escapes")

    args = parser.parse_args()

    output = ' '.join(args.text)

    if args.e:
        output = bytes(output, "utf-8").decode("unicode_escape")

    if args.n:
        print(f"\033[96m{output}\033[0m", end='')
    else:
        print(f"\033[96m{output}\033[0m")

if __name__ == "__main__":
    main()
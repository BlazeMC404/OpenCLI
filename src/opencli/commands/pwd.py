"""
Print the current working directory, similar to Unix `pwd`.
"""
import os
from opencli.config import logger, Colors

def main():
    print(os.getcwd())

if __name__ == '__main__':
    main()
#!/usr/bin/python3
#0-read_file.py
"""reads text file, prints to stdout"""

def read_file(filename=""):
    """prints file to stdout

    Args:
        filename (str): file name
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3

"""reads text file, prints to stdout"""

def read_file(filename=""):
    """prints file to stdout"""
    with open(filename, encoding="utf-8"):
        for line in filename as f:
            print(f.read(), end="")

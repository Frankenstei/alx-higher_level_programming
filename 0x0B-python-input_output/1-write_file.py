#!/usr/bin/python3
#1-write_file.py

"""writes to a file"""

def write_file(filename="", text=""):
    """writes using utf-8 encoding

    Args:
    filename (str): name of file
    text (str): text to copy

    Returns:
    Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
       return (f.write(text))

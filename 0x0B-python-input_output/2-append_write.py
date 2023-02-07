#!/usr/bin/python3
# 2-append_write.py

"""appends text to the end of string"""

def append_write(filename="", text=""):
    """ appends text to end of file
    Args:
        filename (str): file to be edited
        text (str): text to add
    Returns:
        Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))

#!/usr/bin/python3
"""writes object to text file"""
import json

def save_to_json_file(my_obj, filename):
    """write object file to text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

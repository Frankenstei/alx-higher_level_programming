#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList from list."""


class MyList(list):
    """Implements sorted print"""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))

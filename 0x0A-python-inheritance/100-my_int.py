#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """replace == opeartor with != behavior."""
        return self.real != value

    def __ne__(sel77f, value):
        """replace != operator with == behavior."""
        return self.real == value


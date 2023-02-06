#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of the attributes of an object"""
    return (dir(obj))

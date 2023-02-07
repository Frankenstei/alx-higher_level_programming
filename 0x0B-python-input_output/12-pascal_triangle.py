#!/usr/bin/python3
# 12-pascal_triangle.py
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        pascal_tr = pascal[-1]
        tmp = [1]
        for i in range(len(pascal_tr) - 1):
            tmp.append(pascal_tr[i] + pascal_tr[i + 1])
        tmp.append(1)
        pascal.append(tmp)
    return pascal

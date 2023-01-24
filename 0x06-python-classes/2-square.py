#!/usr/bin/python3
"""exception in class"""

class Square:
    """square class"""
    def __init__(self, size=0):
        """size initialization
        
        Args:
           size (int): must be integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""square and private instance atteibute"""

class Square:
    """square class"""

    def __init__(self, size=0):
        """initializing size:

        Args:
          size(int): must be integer
        """
        self.size = size

        @property
        def size(self):
            """Getter and setter"""
            return (self.__size)
        @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        def area(self):
            """ return area """
            return (self.__size * self.__size)
        def my_print(self):
            """ prints # squares """
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
                if self.__size == 0:
                    print("")

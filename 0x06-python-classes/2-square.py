#!/usr/bin/python3
"""A class Square that defines a square"""

class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class

        Args:
            size: The size of the square. Defaults to 0
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

#!/usr/bin/python3
"""class square defines a square"""

class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        """initializes a new instance of the Square class
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """Calculates the area of square.

        Returns: current square area.
        """
        return self.__size ** 2

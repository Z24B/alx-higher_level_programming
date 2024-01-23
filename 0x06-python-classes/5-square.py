#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size: The size of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square

        Returns: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square with the character '#' to stdout.
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))

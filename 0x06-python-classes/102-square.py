#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This class defines the square"""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.
        """
        self.size = size

    def __lt__(self, other):
        """Sets the compare less than behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() <= other.area()

    def __eq__(self, other):
        """Sets the compare equality behavior of the Square object.

        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() == other.area()

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates and returns the area of the square."""

        return self.__size ** 2

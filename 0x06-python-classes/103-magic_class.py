#!/usr/bin/python3
"""Defines a class MagicClass"""


import math


class MagicClass:
    """Class that defines MagicClass"""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass class

        Args:
            radius (int, float): radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return current circle area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return current circle circumference."""
        return 2 * math.pi * self.__radius

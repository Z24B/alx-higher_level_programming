#!/usr/bin/python3
""" a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry with area and integer_validator methods."""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        x = type(value)
        if x != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

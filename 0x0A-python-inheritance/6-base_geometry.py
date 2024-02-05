#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry with an unimplemented area method."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

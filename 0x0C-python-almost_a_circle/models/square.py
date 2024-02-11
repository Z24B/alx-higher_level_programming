#!/usr/bin/python3
"""File containing square.py module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): Optional. The x-coordinate of the square's position.
            y (int): Optional. The y-coordinate of the square's position.
            id (int): Optional. The id for the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

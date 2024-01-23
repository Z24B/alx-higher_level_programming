#!/usr/bin/python3
"""class Square that defines a square"""



class Square:
    """
    This class defines a square.

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size: The size of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Area of square

        Returns: current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute
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

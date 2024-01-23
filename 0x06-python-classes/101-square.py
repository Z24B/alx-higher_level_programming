#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """
    This class defines a square.

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class

        Args:
            __size (int): The size of the square. Defaults to 0.
            __position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates and returns the area of the square.

        Returns: The area of the square.
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
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints square with the character '#' to stdout, using the specified position
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

    def __str__(self):
        """Returns a string representation of the square.

        Returns: The square.
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))

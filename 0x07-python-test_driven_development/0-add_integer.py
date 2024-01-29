#!/usr/bin/python3
"""
This module provides a function for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Casting to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b

# If the script is run standalone, provide some example usage


if __name__ == "__main__":
    print(add_integer(3, 5))  # Output: 8
    print(add_integer(2.5, 3.5))  # Output: 6
    print(add_integer(7, "hello"))  # Raises TypeError: b must be an integer

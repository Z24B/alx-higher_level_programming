#!/usr/bin/python3
"""
This module provides a function for printing a square with the character #.
"""

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

# If the script is run standalone, provide some example usage
if __name__ == "__main__":
    # Example usage as per your main script
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)

    # Example with exceptions
    try:
        print_square(-1)
    except Exception as e:
        print(e)

#!/usr/bin/python3
"""function that prints the list, but sorted ascending sort"""


class MyList(list):
    """Custom class MyList that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))

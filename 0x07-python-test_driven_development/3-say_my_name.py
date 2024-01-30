#!/usr/bin/python3
"""
This module provides a function for printing a name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the formatted string "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted string
    print("My name is {} {}".format(first_name, last_name))

# If the script is run standalone, provide some example usage
if __name__ == "__main__":
    # Example usage as per your main script
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

    # Example with TypeError
    try:
        say_my_name(12, "White")
    except TypeError as e:
        print(e)

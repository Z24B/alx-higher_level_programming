#!/usr/bin/python3
"""File containing function write_file"""


def write_file(filename="", text=""):
    """Writes string to text file(UTF8) and returns number of characters"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

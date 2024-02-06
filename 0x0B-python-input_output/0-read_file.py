#!/usr/bin/python3
"""File containing function for read_file"""


def read_file(filename=""):
    """Reads content of a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

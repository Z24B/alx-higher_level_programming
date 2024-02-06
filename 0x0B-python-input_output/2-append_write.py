#!/usr/bin/python3
"""File containing function append_write"""


def append_write(filename="", text=""):
    """Appends string at end of text file & returns num of characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

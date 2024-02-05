#!/usr/bin/python3
"""function that returns True or False"""


def is_same_class(obj, a_class):
    """return True if obj is instance of a_class"""
    x = type(obj)
    if x == a_class:
        return True
    return False

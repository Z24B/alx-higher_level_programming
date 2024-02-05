#!/usr/bin/python3
"""function that returns True or False"""


def inherits_from(obj, a_class):
    """returns true if obj is an instance of a class, otherwise false"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False

#!/usr/bin/python3
"""function that returns true or false"""


def inherits_from(obj, a_class):
    """returns true if obj is an inherited class"""
    return (issubclass(type(obj), a_class))

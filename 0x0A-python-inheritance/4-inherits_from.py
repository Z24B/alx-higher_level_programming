#!/usr/bin/python3
"""Function that returns true or false"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of class inherited, or False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


if __name__ == "__main__":
    # Test the function
    class ParentClass:
        pass

    class ChildClass(ParentClass):
        pass

    example_object = ChildClass()
    result = inherits_from(example_object, ParentClass)
    print(result)

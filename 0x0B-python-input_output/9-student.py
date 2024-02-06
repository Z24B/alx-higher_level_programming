#!/usr/bin/python3
"""File with class Student that defines a student"""


class Student:
    """Defines a student by first name, last name, and age"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

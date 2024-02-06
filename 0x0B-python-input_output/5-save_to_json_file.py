#!/usr/bin/python3
"""File containing function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()

#!/usr/bin/python3
"""script that adds all arguments to Python list, then saves to file"""
from sys import argv


save_to_json_file = __import__('6-load_from_json_file').load_from_json_file
load_from_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = save_to_json_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

load_from_json_file(json_list, 'add_item.json')

#!/usr/bin/python3
"""file with function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert line of text to file after each line containing specific str"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string + '\n')


    with open(filename, 'w') as file:
        file.writelines(modified_lines)

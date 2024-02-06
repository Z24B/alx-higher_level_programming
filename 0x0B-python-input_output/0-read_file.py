#!/usr/bin/python3


def read_file(filename=""):
    """Reads content of a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

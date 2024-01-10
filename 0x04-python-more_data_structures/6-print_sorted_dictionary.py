#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = list(a_dictionary.keys())
    key.sort()
    for x in key:
        print("{}: {}".format(x, a_dictionary.get(x)))

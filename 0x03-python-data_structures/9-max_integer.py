#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if not size:
        return None
    else:
        x = my_list[0]
        for item in my_list[1:]:
            x = x if item <= x else item
        return x

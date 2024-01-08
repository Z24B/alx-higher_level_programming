#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if int(idx) < 0 or int(idx) + 1 > len(my_list):
        return my_list
    del my_list[idx]
    return my_list

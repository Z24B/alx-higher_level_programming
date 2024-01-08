#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    for char in char_list:
        if char == 'c' or char == 'C':
            char_list.remove(char)
            return("".join(char_list))

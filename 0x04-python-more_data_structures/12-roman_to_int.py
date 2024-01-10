#!/usr/bin/python3

def roman_to_int(roman_string):
    rmn_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    x = 0
    y = 0

    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) -1, -1, -1):
            if rmn_num[roman_string[i]] >= y:
                x += rmn_num[roman_string[i]]
            else:
                x -= rmn_num[roman_string[i]]
            y = rmn_num[roman_string[i]]
    return x

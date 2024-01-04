#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import hidden_4
    for x in dir(hidden_4):
        if x[0] != '_' and x[1] != '_':
            print(x)

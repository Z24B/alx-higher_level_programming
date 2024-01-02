#!/usr/bin/python3
for num in range(0, 10):
    for x in range(num + 1, 10):
        if num == 8 and x == 9:
            print('89')
        else:
            print('{}{}, '.format(num, x), end='')

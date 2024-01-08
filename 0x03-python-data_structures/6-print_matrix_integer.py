#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for column in row:
                print('{:d}'.format(column), end=' '
                      if column != row[-1] else '\n')

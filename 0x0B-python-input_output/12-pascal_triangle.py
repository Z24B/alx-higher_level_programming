#!/usr/bin/python3
"""File with function pascal_triangle: returns integers of Pascal’s triangle"""


def pascal_triangle(n):
    """Create Pascal's triangle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

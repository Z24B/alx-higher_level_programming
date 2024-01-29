#!/usr/bin/python3
"""
N Queens puzzle solution
"""


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve(board, row, n, solutions):
    """
    Solve N Queens problem using backtracking
    """
    if row == n:
        solution = [[r, c] for r, c in enumerate(board)]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n, solutions)


def print_solutions(n):
    """
    Print all solutions for the N Queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print_solutions(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

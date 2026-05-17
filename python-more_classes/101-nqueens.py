#!/usr/bin/python3
"""Solves the N queens problem"""

import sys


def is_safe(board, row, col, n):
    """Check if position board[row][col] is safe"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def print_solution(board, n):
    """Print matrix board"""
    solution = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def solve(board, row, n):
    """Solve the board with backtraking"""
    if row == n:
        print_solution(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
board = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)
solve(board, 0, n)

#!/usr/bin/python3
"""This module contains a pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n"""
    new_list = []
    row = []
    if n <= 0:
        return new_list
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = new_list[i - 1]
            for j in range(len(prev_row) - 1):
                number = prev_row[j] + prev_row[j + 1]
                row.append(number)
            row.append(1)
        new_list.append(row)
    return new_list

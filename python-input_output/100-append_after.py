#!/usr/bin/python3
""" function that inserts a line of text to a file,"""
"""after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a new string after a specific string"""
    with open(filename, "w") as f:
        result = ""
        for i in f:
            result += i
            if search_string in i:
                result += new_string

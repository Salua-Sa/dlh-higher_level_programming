#!/usr/bin/python3
"""This module contains an Square class."""


class Square:
    """This class Square defines a square with size."""

    def __init__(self, size=0):
        """Initializes a Square with a given size and specific conditions:
        1) size must be an integer, otherwise raise a
        TypeError exception with the message size must be an integer.
        2) if size is less than 0, raise a ValueError
        exception with the message size must be >= 0

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

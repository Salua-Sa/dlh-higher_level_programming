#!/usr/bin/python3
"""This module contains a Square class."""


class Square:
    """This class defines a square with size."""

    def __init__(self, size=0):
        """Initializes a Square with a given size and specific conditions."""

        @property
        def size(self):
            """Retrieves the size of the square."""
            return self.__size

        @size.setter
        def size(self, value):
            """Sets the size of the square."""
            self.__size = value

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the current square area."""
        return self.__size * self.__size

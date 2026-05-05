#!/usr/bin/python3
"""This module contains an Square class."""


class Square:
    """This class defines a square with size."""

    
    def __init__(self, size=0):
        """Initializes a Square with a given size and specific conditions."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

 
    def area(self):
        """This method returns the square area."""
        return self.__size * self.__size

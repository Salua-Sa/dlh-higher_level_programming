#!/usr/bin/python3
"""This module contains a Square class."""


class Square:
    """This class defines a square with size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square with a given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (type(value) is not tuple or len(value) != 2 or value[0] < 0 or
                type(value[0]) is not int or value[1] < 0 or
                type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

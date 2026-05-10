#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """This class defines a square with size."""

    def __init__(self, size=0):
        """Initializes a Square with a given size."""
        self.size = size

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

    def area(self):
        """This method returns the current square area."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Method equal comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method not equal comparator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Method greater comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method greater or equal comparator"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Method less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Method less or equal comparator"""
        return self.area() <= other.area()

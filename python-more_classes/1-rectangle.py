#!/usr/bin/python3
"""This File contains an empty Rectangle class"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Square with a given width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @widht.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__size = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @hight.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__size = value

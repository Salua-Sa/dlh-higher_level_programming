#!/usr/bin/python3
"""This module contains an Student class."""


class Student:
    """Defines a student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Initializes a Student with a given first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) is not list:
            return self.__dict__
        else:
            new_dictionary = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dictionary[key] = self.__dict__[key]
            return new_dictionary

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json().items:
            setattr(self, key, value)

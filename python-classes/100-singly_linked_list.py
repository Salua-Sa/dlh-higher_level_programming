#!/usr/bin/python3
""" class Node that defines a node of a singly linked list"""


class Node:
    def __init__(self, data, next_node=None):
        """Initializes a Node with a given data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list"""
    def __init__(self):
        """Initializes a head"""
        self.__head = None

    def __str__(self):
        """Return the result"""
        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted"""
        new_node = Node(value)
        if self.__head is None or value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None
               and value >= current.next_node.data):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
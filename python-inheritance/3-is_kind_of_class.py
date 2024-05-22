#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if the object is an instance of a class that inherited from, the specified class.
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)

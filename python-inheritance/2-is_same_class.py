#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

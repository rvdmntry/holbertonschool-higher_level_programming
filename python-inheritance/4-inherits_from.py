#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited (directly or indirectly) from a_class.
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""
0-lookup module
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    :param obj: The object to inspect.
    :return: A list of attributes and methods.
    """
    return dir(obj)

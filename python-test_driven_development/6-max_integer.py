#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.

    Args:
        list (list): The list of integers to search.

    Returns:
        int: The maximum integer in the list. If the list is empty, returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]
    return result

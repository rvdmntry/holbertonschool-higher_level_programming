#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.

    Args:
        a: The first number, expected to be an integer or a float.
        b: The second number, expected to be an integer or a float. Defaults to 98.

    Returns:
        The integer addition of a and b after casting them to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf') or b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a != a or b != b:  # NaN check
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)

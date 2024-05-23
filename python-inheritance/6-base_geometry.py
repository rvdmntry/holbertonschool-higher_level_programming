#!/usr/bin/python3
"""
6-base_geometry module
"""


class BaseGeometry:
    """
    A class BaseGeometry with a method area that raises an exception.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""
7-base_geometry module
"""


class BaseGeometry:
    """
    A class BaseGeometry with methods area and integer_validator.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        :param name: The name of the parameter (assumed to be a string).
        :param value: The value to validate.
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

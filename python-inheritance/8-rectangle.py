#!/usr/bin/python3
"""
8-rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    Instantiation with width and height, validated by integer_validator.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

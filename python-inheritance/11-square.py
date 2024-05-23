#!/usr/bin/python3
"""
11-square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    Instantiation with size, validated by integer_validator.
    """

    def __init__(self, size):
        """
        Initialize a new Square.
        :param size: The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        :return: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the square description.
        :return: A string describing the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

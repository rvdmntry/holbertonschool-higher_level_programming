#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    A class that defines a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with keys as public
            attribute names and values as their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)

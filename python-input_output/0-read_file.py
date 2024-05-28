#!/usr/bin/python3
"""
This module provides a function to read a text file and print its content.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

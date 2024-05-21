#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ?, :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in chars:
            new_text += "\n\n"

    lines = [line.strip() for line in new_text.split("\n")]
    for line in lines:
        print(line, end="")
        if line != lines[-1]:
            print()

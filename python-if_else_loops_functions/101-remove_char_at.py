#!/usr/bin/env python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):  # Check if index is out of bounds
        return str
    new_str = ""  # Start with an empty string to build the new version
    for i in range(len(str)):
        if i != n:  # Append the character only if it's not at the index n
            new_str += str[i]
    return new_str


if __name__ == "__main__":
    remove_char_at = __import__('101-remove_char_at').remove_char_at

    print(remove_char_at("Best School", 3))  # "Bes School"
    print(remove_char_at("Chicago", 2))      # "Chcago"
    print(remove_char_at("C is fun!", 0))    # " is fun!"
    print(remove_char_at("School", 10))      # "School"
    print(remove_char_at("Python", -2))      # "Python"

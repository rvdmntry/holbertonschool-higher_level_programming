#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get a list of keys sorted in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print key-value pairs
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")

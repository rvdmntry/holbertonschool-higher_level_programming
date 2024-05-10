#!/usr/bin/python3
import sys
import os

def list_module_names():
    # Ensure the module is available in the Python search path
    sys.path.append('/tmp/')
    # Import the module by its name without the '.pyc' extension
    import hidden_4

    names = dir(hidden_4)  # List all names defined by the module
    filtered_names = [name for name in names if not name.startswith('__')]
    # Print filtered names in alphabetical order
    for name in sorted(filtered_names):
        print(name)

if __name__ == "__main__":
    list_module_names()

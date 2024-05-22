#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))

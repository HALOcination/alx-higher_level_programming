#!/usr/bin/python3
"""class MyList that inherits from list"""


class Mylist(list):
    """class that inherits from list"""
    def print_sorted(self):
        """that prints a sorted list
        """
        print(sorted(self))

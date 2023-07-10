#!/usr/bin/python3
"""function only sub class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class"""

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False

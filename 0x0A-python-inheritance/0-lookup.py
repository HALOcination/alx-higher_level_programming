#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """a function that returns the list of available attributes and methods"""
    return (dir(obj))

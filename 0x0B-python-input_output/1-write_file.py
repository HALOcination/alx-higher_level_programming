#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

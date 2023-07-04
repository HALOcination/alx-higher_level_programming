#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after certain char"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    ind = 0
    textlen = len(text)
    while ind < textlen:
        start = ind
        while start < textlen and text[start] == ' ':
            start += 1
        ind = start
        while (ind < textlen and text[ind] != '.' and text[ind] != ':' and
               text[ind] != '?'):
            ind += 1
        if ind < textlen:
            ind += 1
        print(text[start:ind], ind="")
        ind -= 1
        if text[ind] == '.' or text[ind] == '?' or text[ind] == ':':
            print("\n")
        ind += 1

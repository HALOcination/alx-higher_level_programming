#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_keys = list(a_dictionary.keys())
    ord_keys.sort()
    for n in ord_keys:
        print("{}: {}".format(n, a_dictionary.get(n)))

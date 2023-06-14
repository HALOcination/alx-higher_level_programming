#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_keys = list(a_dictionary.keys())
    ord_keys.sort()
    for n in list_ord:
        print("{}: {}".format(n, a_dictionary.get(n)))

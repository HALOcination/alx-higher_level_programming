#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            char = 32
        else:
            char = 0
        print("{:c}".format(ord(str[i]) - char), end='')
    print()

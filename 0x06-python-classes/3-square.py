#!/usr/bin/python3
""" defines a class square"""


class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be positive')
        else:
            self.__size = size  #: size of square

    def area(self):
        """returns the area

        Returns:
            area square
        """
        return self.__size**2

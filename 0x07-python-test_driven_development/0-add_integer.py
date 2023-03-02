#!/usr/bin/python3
import math
""" math module """


def add_integer(a, b=98):
    """ Addition function """

    if type(a) is float:
        a = math.floor(a)
    if type(b) is float:
        b = math.floor(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

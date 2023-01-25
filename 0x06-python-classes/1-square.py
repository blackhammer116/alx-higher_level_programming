#!/usr/bin/python3
"""creating a private instace attribute"""


class Square():
    """class Square with a private instance attribute"""
    def __init__(self, size):
        self.__size = size

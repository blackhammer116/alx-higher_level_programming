#!/usr/bin/python3
"""creating a private instace attribute"""


class Square():
    """class Square with a private instance attribute
        and checks the validity"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        except (TypeError):
            raise TypeError('size must be an integer')

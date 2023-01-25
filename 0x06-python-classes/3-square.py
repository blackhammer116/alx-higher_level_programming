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
            if type(size) is not int:
                raise TypeError('size must be an integer')
        except (TypeError):
            raise TypeError('size must be an integer')

    def area(self):
        if self.__size:
            return self.__size ** 2
        else:
            return

#!/usr/bin/python3
"""  defining a class rectangle and making it represent
    graphicaly
"""


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """ initalizing the parameters
            Args:
                width (int): width of the class
                height (int): height of the class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width
            Args:
                value (int): value to be setted
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height
            Args:
                value (int): value to be setted
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        r = ""
        
        if self.width == 0 or self.height == 0:
            return r
        for j in range(self.height):
            for i in range(self.width):
                r += "#"

            if j != self.height - 1:
                r += "\n"
        return r

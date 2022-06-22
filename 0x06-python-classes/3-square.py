#!/usr/bin/python3
"""Define a square"""

class Square:
    """class that define a square based o 2-square"""

    
    def __init__(self, size=0):
        """initializing instant attribute size.
        Args:
            size (int): the size of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

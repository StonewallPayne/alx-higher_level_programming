#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of a side of the square"""
    def __init__(self, size=0):

        """Initializes square's size
        Args:
            size (int): size of a side of the square"""
        self.__size = size

    def area(self):
        """Calculates the square's area
        Returns:
            The square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of __size
        Args:
            new_size (int): the size of a size of the square
        """
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

        def my_print(self):
            """Prints in stdout the square with the character #"""
            if self.__size > 0:
                for column in range(self.__size):
                    for row in range(self.__size):
                        print("#", end="")
                    print()
            else:
                print()

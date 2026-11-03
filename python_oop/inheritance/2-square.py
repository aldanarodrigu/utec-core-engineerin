#!/usr/bin/env python3
"""Define a Square class with its own string representation."""

BaseSquare = __import__('1-square').Square


class Square(BaseSquare):
    """Represent a square."""

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

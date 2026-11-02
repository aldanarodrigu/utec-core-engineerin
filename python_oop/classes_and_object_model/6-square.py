#!/usr/bin/env python3
"""Define a Square class with a position and a string representation."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, validating type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, validating it is a tuple of 2 positive ints."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        print(str(self))

    def __str__(self):
        """Return the square as a string (same output as my_print)."""
        if self.__size == 0:
            return ""

        lines = [" " * self.__position[0] + "#" * self.__size
                 for _ in range(self.__size)]
        return "\n" * self.__position[1] + "\n".join(lines)

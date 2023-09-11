#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """Represents the geometry"""

    def area(self):
        """Define anarea of a shape

        Raises:
            Exemption: area() is not implemented
        """
        raise Exception("area() is not implemented")

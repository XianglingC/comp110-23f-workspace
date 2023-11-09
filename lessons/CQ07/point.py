"""Create point class."""
from __future__ import annotations

__author__ = "730658974"


class Point:
    """New class of point."""
    x: float
    y: float

    # constructor
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Define the Init function."""
        self.x = x_init
        self.y = y_init

    # def mutating method
    def scale_by(self, factor: int) -> None:
        """Define the mutating function with return type of Point."""
        self.x *= factor
        self.y *= factor

    # def mutating method point#scale
    def scale(self, factor: int) -> Point:
        """Creating a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    # CQ08 0:__str__() Magic method
    def __str__(self) -> str:
        """Make the output redable."""
        output: str = f"x: {self.x}; y: {self.y}"
        # output: str = f"x:{self.x}; y:{self.y}" also works
        return output
    
    # CQ08 __mul__()
    def __mul__(self, factor: int | float) -> Point:
        """Multiply the factor and creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    # CQ08 2:__add__()
    def __add__(self, add: int | float) -> Point:
        """Overloading add operator."""
        new_point: Point = Point(self.x + add, self.y + add)
        return new_point

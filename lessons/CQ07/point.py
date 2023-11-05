"""Create point class."""
from __future__ import annotations

__author__ = "730658974"


class Point:
    """New class of point."""
    x: float
    y: float

    # constructor
    def __init__(self, x_init: float, y_init: float):
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

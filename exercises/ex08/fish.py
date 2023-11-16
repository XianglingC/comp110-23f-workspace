"""File to define Fish class."""

__author__ = "730658974"


class Fish:
    """fish."""
    age: int

    # 2.2
    def __init__(self):
        """Change of day."""
        self.age = 0
        return None
    
    def one_day(self):
        """Age."""
        self.age += 1
        return None
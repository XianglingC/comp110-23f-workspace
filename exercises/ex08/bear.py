"""File to define Bear class."""

__author__ = "730658974"


class Bear:
    """Bear."""
    age: int
    hunger_score: int

    # 1.2 Bear
    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Change of fish."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Eat!"""
        self.hunger_score += num_fish
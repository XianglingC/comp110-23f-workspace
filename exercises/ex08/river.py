"""File to define River class."""

__author__ = "730658974"
from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River."""
    day: int  # Tells you what day of the river's lifecycle you're modeling
    bears: list  # bear population
    fish: list  # fish population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check the ages and remove them."""
        new_fish: list[Fish] = []
        for current_fish in self.fish:  # Does self.fish here refers to the self.fish list in the __init__?
            if current_fish.age <= 3:
                new_fish.append(current_fish)
        self.fish = new_fish
        new_bear: list[Bear] = []
        for current_bear in self.bears:
            if current_bear.age <= 5:
                new_bear.append(current_bear)
        self.bears = new_bear
        return None

    def remove_fish(self, amount: int):
        """Remove amount of fish."""
        counter: int = 0
        while counter < amount:
            self.fish.pop(0)
            counter += 1

    def bears_eating(self):
        """Modify the bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Check starved bear."""
        survive_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survive_bear.append(bear)
        self.bears = survive_bear
        return None
        
    def repopulate_fish(self):
        """Reproduce the fish."""
        new_fish: int = (len(self.fish) // 2) * 4
        for fish in range(0, new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Reproduce the bears."""
        new_bears: int = len(self.bears) // 2
        for bear in range(0, new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Formatting."""
        print(f"~~~ Day {self.day}: ~~~")
        fish_p: int = len(self.fish)
        bear_p: int = len(self.bears)
        print(f"Fish population: {fish_p}")
        print(f"Bear population: {bear_p}")
        return None

    def one_river_week(self):  
        """7 days for the river.""" 
        counter: int = 1
        while counter < 8:
            self.one_river_day()
            counter += 1
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            

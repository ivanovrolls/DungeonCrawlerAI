from abc import ABC, abstractmethod

class item:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    @abstractmethod
    def stats(self, player):
        """Each item type must implement this method."""
        pass

    @abstractmethod
    def active(self, player):
        """Each item type must implement this method."""
        pass

class HealingPotion(item):
    def __init__(self, name, stats):
        super().__init__(name, stats)

    def use(self, player):
        healing = self.stats.get("health", 0)
        player.health += healing
        print(f"{player.name} used {self.name} and restored {healing} health!")


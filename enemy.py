class Enemy:
    def __init__(self, name, health=100, ad=10):
        self.name = name
        self.health = health
        self.ad = ad
        self.inventory = []

    def attack(self, player):
        damage = self.ad
        player.take_damage(damage)
        print(f"{self.name} attacked {player.name} for {damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage. Remaining health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            
    @abstractmethod
    def use_ability(self):
        """Each enemy type must implement this method."""
        pass

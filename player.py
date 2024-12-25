class Player:
    def __init__(self, name, health=100, ad=10):
        self.name = name
        self.health = health
        self.ad = ad
        self.inventory = []

    def attack(self, enemy):
        damage = self.ad
        enemy.take_damage(damage)
        print(f"{self.name} attacked {enemy.name} for {damage} damage!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage. Remaining health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def use_item(self, item):
        if item in self.inventory:
            item.apply_effect(self)
            self.inventory.remove(item)
        else:
            print("Item not found in inventory.")

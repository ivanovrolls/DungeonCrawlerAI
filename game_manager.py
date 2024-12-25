from dungeon import Dungeon
from player import Player

class GameManager:
    def __init__(self):
        self.player = None
        self.dungeon = Dungeon()

    def start_game(self):
        print("Welcome to the Dungeon Crawler!")
        name = input("Enter your character's name: ")
        self.player = Player(name)
        self.dungeon.generate_map()
        self.main_loop()

    def main_loop(self):
        while self.player.health > 0:
            self.dungeon.display_current_room()
            action = input("What do you want to do?: ")
            if action == "quit":
                print("Thanks for playing!")
                break
            self.process_action(action)

    def process_action(self, action):
        if action == "move":
            direction = input("Which direction?: ")
            self.dungeon.move_player(direction)
        elif action == "attack":
            enemy = self.dungeon.get_enemy_in_room()
            if enemy:
                self.player.attack(enemy)
            else:
                print("No enemies here!")
        elif action == "use item":
            print("Your inventory:", self.player.inventory)
            item_name = input("Which item to use?: ")
            item = next((i for i in self.player.inventory if i.name == item_name), None)
            if item:
                self.player.use_item(item)
            else:
                print("Item not found!")
        else:
            print("Invalid action.")

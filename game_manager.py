from dungeon import Dungeon
from player import Player
import spacy

class GameManager:
    def __init__(self):
        self.player = None
        self.dungeon = Dungeon()
        self.nlp = spacy.load("en_core_web_sm")
        self.player_position = None  #track the player's current position



    def start_game(self):
        print(f"Welcome to the Dungeon Crawler, {self.player.name}!")
        if self.dungeon.start_position:
            self.player_position = self.dungeon.start_position
        else:
            print("No rooms generated in the dungeon!")
            return
        self.main_loop()

    def main_loop(self):
            while self.player.health > 0:
                self.dungeon.display_current_room(self.player_position)

                # Get and display valid neighboring rooms
                neighbors = self.dungeon.get_neighboring_rooms(self.player_position)
                print("You can move to the following rooms:")
                for neighbor in neighbors:
                    print(f"- Room at ({neighbor['x']}, {neighbor['y']})")

                print(f"Player Health: {self.player.health}")
                print(f"Inventory: {self.player.inventory}")

                action = input("What do you want to do?: ")
                if action == "quit":
                    print("Thanks for playing!")
                    break
                self.process_action(action)

    def process_action(self, input_text):
        doc = self.nlp(input_text)

        action = None
        target = None

        for token in doc:
            if token.pos_ == "VERB" and not action:
                action = token.lemma_ 
            elif token.pos_ == "NOUN" and not target:
                target = token.text

        if action == "move":
            self.handle_move(input_text)
        elif action == "attack":
            self.handle_attack(target)
        elif action == "use":
            self.handle_use_item(target)
        else:
            print("I don't understand that command.")

    def handle_move(self, input_text):
        direction = ["north", "south", "east", "west"]
        doc = self.nlp(input_text)

        direction = next((token.text for token in doc if token.text in directions), None)
        if direction:
            self.dungeon.move_player(direction)
        else:
            print("Please specific a valid location.")

    def handle_attack(self, target):
        enemy = self.dungeon.get_enemy_in_room()
        if enemy and target and target.lower() in enemy.name.lower():
            self.player.attack(enemy)
            if enemy.health > 100:
                print(f"{enemy.name} has {enemy.health} remaining.")
            else:
                print(f"{enemy.mean} is defeated.")
        else:
            print("No enemy found.")

    def handle_use_item(self, target):
        if not self.player.inventory:
            print("Your inventory is empty!")
            return
        item = next((i for i in self.player.inventory if i.name.lower() == target.lower()), None)
        if item:
            self.player.use_item(item)
            print(f"You used {item.name}.")
        else:
            print("Item not found in your inventory.")
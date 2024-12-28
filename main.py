from game_manager import GameManager
from player import Player
from dungeon import Dungeon
from item import HealingPotion
from enemy import FireSprite  # Example enemies

def setup_game():
    """Set up the game with a dungeon, player, and enemies."""
    # Initialize the game manager
    game_manager = GameManager()

    # Create the player
    player_name = input("Enter your character's name: ")
    player = Player(name=player_name, health=100, ad=15)
    game_manager.player = player

    # Create the dungeon
    dungeon = Dungeon(width=5, height=5)
    dungeon.generate_layout()
    game_manager.dungeon = dungeon

    # Add items to the player inventory
    potion = HealingPotion(name="Health Potion", stats={"health": 25})
    player.inventory.extend([potion])

    # Add enemies
    fire_enemy = FireSprite(name="Flame Demon", health=120, ad=20)
    dungeon.rooms.append({"x": 1, "y": 1, "enemy": fire_enemy, "type": "enemy"})
    return game_manager

def main():
    """Main entry point for the game."""
    print("Welcome to the Dungeon Crawler Game!")
    game_manager = setup_game()

    # Display dungeon layout and description
    print("\nDungeon Layout:")
    game_manager.dungeon.display_map()
    print("\nDungeon Description:")
    print(game_manager.dungeon.describe_dungeon())

    # Start the game loop
    game_manager.start_game()

if __name__ == "__main__":
    main()

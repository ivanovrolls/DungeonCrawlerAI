class npc:
    def __init__(self, name, location, dialogue):
        self.name = name
        self.location = location
        self.dialogue = dialogue

    def talk(self):
        for i, line in enumerate(self.dialogue, 1):
            print(f"{i}: {line}")
        choice = input("Choose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.dialogue):
            print(f"{self.name}: {self.dialogue[int(choice) - 1]}")

    def interact(self, player):
        print(f"You are interacting with {self.name}.")
        self.talk()

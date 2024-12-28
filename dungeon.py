import random
from openai import OpenAI
import os

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

class Dungeon:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.layout = [[" " for _ in range(width)] for _ in range(height)]
        self.rooms = []
        self.description = "" #GPT generated

    def generate_layout(self):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < 0.33: #33% chance to spawn a room
                    self.layout[y][x] = "R" 
                    self.rooms.append({"x": x, "y": y, "type": random.choice(["enemy", "treasure", "empty"])})

    def display_map(self):
        for row in self.layout:
            print(" ".join(row))

    def describe_dungeon(self):
        room_descriptions = []
        for room in self.rooms:
            x, y, room_type = room["x"], room["y"], room["type"]
            room_descriptions.append(f"A {room_type} room at ({x}, {y}).")

        layout_summary = f"The dungeon has {len(self.rooms)} rooms. The layout is:\n" + "\n".join(room_descriptions)
        prompt = (
            "You are a dungeon master creating an evocative description of a dungeon for an AI Powered dungeon crawler game. "
            "Each room contains one thing, either nothing, an enemy or a treasure."
            "Based on the following layout details, describe the dungeon in a way that immerses the reader:\n\n"
            f"{layout_summary}\n\n"
            "Dungeon Description:"
        )

        self.description = self.generate_with_gpt(prompt)
        return self.description

    def generate_with_gpt(self, prompt):
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a creative dungeon master."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,  # Adjust token limit as needed
                temperature=0.7  # Adjust creativity level as needed
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print("Error generating description:", e)
            return "An ancient dungeon shrouded in mystery, with countless secrets to uncover."

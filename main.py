import pygame
import sys
import json
from gpt import generate

pygame.init()

# Replace with the actual path to your Space Mono font file
font_path = "C:\\Users\\senthil\\Downloads\\Space_Mono.zip\\SpaceMono-Regular.ttf"
font_size = 24  # Adjust the size as needed

space_mono_font = pygame.font.Font(font_path, font_size)

# Corrected the screen dimensions
screen = pygame.display.set_mode([800, 600])

# Load an image or provide a valid path to an image file
bg = pygame.image.load("image0.jpg")  # Adjust the image file extension

running = True

pygame.font.init()  # Corrected the method call

class Rpg:
    def __init__(self, filename, name, loadfromfile=False):
        self.filename = filename
        if not loadfromfile:
            history = f"This is the ancient world of Draconia. {name}'s village has been attacked by a dragon named Drakonir. To defend their village, they must journey into the forest and defeat the great beast.\nCompleted goals:\n"
            self.data = {"name": name, "xp": 0,
                         "goal": generate(f"generate the next goal for {name} with 0 xp based on {history}"),
                         "history": history,
                         "goalscompleted": 0,
                         "monsname": ""}
        else:
            with open(filename, 'r') as openfile:
                self.data = json.load(openfile)

    def getNextGoal(self):
        self.data["goalscompleted"] += 1
        self.data["history"] += f"goal {self.data['goalscompleted']}. {self.data['goal']}\n"
        nextgoal = generate(f"generate the next goal for {self.data['name']} with {self.data['xp']} based on {self.data['history']}")
        self.data["goal"] = nextgoal

    def getMonster(self):
        self.data["monsname"] = generate(f"generate the name for the monster")
        # Placeholder code, replace with actual code to generate monster characteristics
        self.data["monster"] = generate(f"generate characteristics for {self.data['monsname']}")

# Create an instance of the Rpg class
rpg_instance = Rpg("savefile.json", "PlayerName", loadfromfile=True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Blit the background image onto the screen
    screen.blit(bg, (0, 0))

    pygame.display.update()

    name = input("What is your character's name?")

    # Use the render_text function to render text
    render_text(name, font_path, font_size, (255, 255, 255), (100, 100))

    print("Welcome to the ancient world of Draconia, " + name + ". Your village has been attacked by a dragon named Drakonir. To defend your village, you must journey into the forest and defeat the great beast. But you are weak. Can you level up in time?...")

    # Generate and print the next goal
    rpg_instance.getNextGoal()
    print(f"Next goal: {rpg_instance.data['goal']}")

    # Generate and print the monster name and characteristics
    rpg_instance.getMonster()
    print(f"A wild {rpg_instance.data['monsname']} appears!\nCharacteristics: {rpg_instance.data['monster']}")

    pygame.display.flip()
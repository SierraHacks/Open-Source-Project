import pygame, sys, json
from gpt import generate
pygame.init()
font_path = "C:\Users\senthil\Downloads\Space_Mono.zip\SpaceMono-Regular.ttf"  # Replace with the actual path to your Space Mono font file
font_size = 24  # Adjust the size as needed

space_mono_font = pygame.font.Font(font_path, font_size)


screen=pygame.display.pygame.display.set_mode([100, 100])
bg = pygame.image.load("image0")
running = True

pygame.font.init
class Rpg:
    def __init__(self,filename,name,loadfromfile=False):
        self.filename = filename
        if not loadfromfile:
            history = f"This is the ancient world of Draconia. {name}'s village has been attacked by a dragon named Drakonir. To defend their village, they must journey into the forest and defeat the great beast.\nCompleted goals:\n"
            self.data = {"name":name,"xp":0,
                         "goal": generate(f"generate the next goal for {name} with 0 xp based on {history}"),
                         "history":history,
                         "goalscompleted":0}
        else:
            with open(filename, 'r') as openfile:
                self.data = json.load(openfile)
        pass
    def getNextGoal(self):
        self.data["goalscompleted"]+=1
        self.data["history"]+= f"goal {self.data["goalscompleted"]}. {self.data["goal"]}\n"
        nextgoal = generate(f"generate the next goal for {self.data["name"]} with {self.data["xp"]} based on {self.data["history"]}")
        self.data["goal"]=nextgoal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
     # Blit the background image onto the screen
    screen.blit(bg, (0, 0))

    pygame.display.update()

    name = input("What is your character's name?")
    print ("Welcome to the ancient world of Draconia, " + name + ". Your village has been attacked by a dragon named Drakonir. To defend your village, you must journey into the forest and defeat the great beast. But you are weak. Can you level up in time?...")
    XP = 0
    print ("You must defeat a Golem named Goro to venture into the forest. Navigate treacherous passages, decipher ancient runes to uncover the Golem's weakness, and prepare for a formidable battle. Evade its earth-shattering strikes, exploit its vulnerability, and triumph. You need 50 XP to defeat Goro.")
    if XP >= 50:
        print ("Congratulations! You have defeated Goro the Golem and can now enter the forest. But you must journey into the tangled depths of the Forest, where Arachno, the spider queen's lair lies hidden amidst silken threads and shadowed groves. Navigate the labyrinthine paths, evade venomous traps, and overcome her arachnid minions to reach the heart of the Queen's domain. You need 100 XP to defeat Arachno")
    
    if XP >= 100:
        print ("After training for months, you have defeated Arachno the Spider Queen, and can now enter the dragons cave itself. But are you ready? You need 150 XP to defeat the dragon.")
    if XP >= 150:
        print ("You enter the cave. The dragon loomed, scales aglow with fiery power. Its breath seared the air, but your agility kept you safe among ancient ruins. Sword in hand, you engaged in a fierce duel. Dodging claws, you struck where scales thinned. The dragon roared, wings thrashing, trying to unbalance you.With unwavering resolve, you seized an opening and drove your blade true. The dragon, defeated, fell with a thunderous crash, vanquished by your bravery and skill. But then, you see another dragon flying into the cave, this time an Ice Dragon. You need 300 XP to defeat the Ice Dragon.")

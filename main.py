import pygame, sys, json
from gpt import generate
pygame.init()
screen=pygame.display.pygame.display.set_mode([100, 100])
bg = pygame.image.load("image0")
running = True

class Rpg:
    def __init__(self,filename,name,loadfromfile=False):
        self.filename = filename
        if not loadfromfile:
            history = f"This is the ancient world of Draconia. {name}'s village has been attacked by a dragon named Alex. To defend their village, they must journey into the forest and defeat the great beast.\nCompleted goals:\n"
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
    name = input("What is your character's name?")
    print ("Welcome to the ancient world of Draconia, " + name + ". Your village has been attacked by a dragon named Alex. To defend your village, you must journey into the forest and defeat the great beast. But you are weak. Can you level up in time?...")

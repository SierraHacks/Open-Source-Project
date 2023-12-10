import pygame, sys, json
pygame.init()
screen=pygame.display.pygame.display.set_mode([100, 100])
bg = pygame.image.load("image0")
running = True

class Rpg:
    def __init__(self,filename,name,loadfromfile=False):
        self.filename = filename
        if not loadfromfile:
            self.data = {"name":name,"xp":0,"goal":""}
        else:
            with open(filename, 'r') as openfile:
                self.data = json.load(openfile)
        pass
    def getNextGoal(self):
        pass
    def 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
    name = input("What is your character's name?")
    print ("Welcome to the ancient world of Draconia, " + name + ". Your village has been attacked by a dragon named Alex. To defend your village, you must journey into the forest and defeat the great beast. But you are weak. Can you level up in time?...)
    

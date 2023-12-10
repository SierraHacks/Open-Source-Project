import pygame
import sys
pygame.init()
screen=pygame.display.pygame.display.set_mode([100, 100])
bg = pygame.image.load("image0")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


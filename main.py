import pygame
import sys
pygame.init()
screen=pygame.display.pygame.display.set_mode([100, 100])
bg = pygame.image.load("image0")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()
import pygame
pygame.init()
screen=pygame.display.pygame.display.set_mode([100, 100])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
bg = pygame.image.load("image0")
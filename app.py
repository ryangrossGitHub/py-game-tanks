import pygame, sys
from pygame.locals import *
import random
from Player import Player
from Globals import Globals
from Obstacle import Obstacle
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLACK = (0, 0, 0)
 
# Screen information
DISPLAY_INFO = pygame.display.Info()
Globals.SCREEN_WIDTH = DISPLAY_INFO.current_w
Globals.SCREEN_HEIGHT = DISPLAY_INFO.current_h - 75
 
DISPLAYSURF = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
pygame.display.set_caption("Tanks")
    
P1 = Player()

trees = pygame.sprite.Group()
for i in range(10):
    tree = Obstacle()
    trees.add(tree)
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()

    DISPLAYSURF.fill(BLACK)
    trees.draw(DISPLAYSURF)
    P1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
import pygame, sys
from pygame.locals import *
import random
from Player import Player
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
DISPLAY_INFO = pygame.display.Info()
SCREEN_WIDTH = DISPLAY_INFO.current_w
SCREEN_HEIGHT = DISPLAY_INFO.current_h - 75
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Tanks")
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/PNG/Tanks/tankRed.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
    
P1 = Player()
E1 = Enemy()

def check_collisions():
    # Projectile collision detection
    for projectile in P1.projectile_group:
        if pygame.sprite.collide_rect(projectile, P1):  # Check for collision
            while True:
                pygame.time.wait(5000)
                P1.projectile_group.empty()
                break
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    # E1.move()

    check_collisions()
    DISPLAYSURF.fill(BLACK)
    P1.draw(DISPLAYSURF)
    # E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
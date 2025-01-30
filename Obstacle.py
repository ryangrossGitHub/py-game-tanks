import pygame
from pygame.locals import *
from Globals import Globals
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/PNG/Environment/treeLarge.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, Globals.SCREEN_WIDTH), random.randint(0, Globals.SCREEN_HEIGHT))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
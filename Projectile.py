import pygame
from pygame.locals import *
import math
from Movement import Movement
from Globals import Globals

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.Surface([16, 16], pygame.SRCALPHA)
        pygame.draw.circle(self.image, (126, 133, 132), (8, 8), 8)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.angle = angle
        self.speed = 7
        self.bounce_count = 0  # Keep track of bounces

    def update(self):
        self.move_forward()

        if self.rect.left < 0:
            self.bounce_count += 1
            self.angle = 180 - self.angle #Reverse horizontal angle
        elif self.rect.right > Globals.SCREEN_WIDTH:
            self.bounce_count += 1
            self.angle = 180 - self.angle #Reverse horizontal angle
        elif self.rect.top < 0:
            self.bounce_count += 1
            self.angle = -self.angle #Reverse vertical angle
        elif self.rect.bottom > Globals.SCREEN_HEIGHT:
            self.bounce_count += 1
            self.angle = -self.angle #Reverse vertical angle

        if self.bounce_count > 2:  # Kill after two bounces
            self.kill()

    def move_forward(self):
        self.rect.x = Movement.calc_move_x(self.speed, self.angle, self.rect.x)
        self.rect.y = Movement.calc_move_y(self.speed, self.angle, self.rect.y)
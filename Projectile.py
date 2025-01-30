import pygame
from pygame.locals import *
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.Surface([16, 16], pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (8, 8), 8)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.angle = angle
        self.speed = 7
        self.bounce_count = 0  # Keep track of bounces

    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))
        self.rect.x += dx
        self.rect.y -= dy

        if self.rect.left < 0:
            self.bounce_count += 1
            self.angle = 180 - self.angle #Reverse horizontal angle
        elif self.rect.right > SCREEN_WIDTH:
            self.bounce_count += 1
            self.angle = 180 - self.angle #Reverse horizontal angle
        elif self.rect.top < 0:
            self.bounce_count += 1
            self.angle = -self.angle #Reverse vertical angle
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.bounce_count += 1
            self.angle = -self.angle #Reverse vertical angle

        if self.bounce_count > 2:  # Kill after two bounces
            self.kill()
import pygame
from pygame.locals import *
import math
from Projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/PNG/Tanks/tankBlue.png").convert_alpha()
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.original_image = pygame.transform.scale(self.original_image, (40, 40))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.angle = 0
        self.speed = 3  # Add a speed attribute
        self.projectile_group = pygame.sprite.Group()  # Group for projectiles
        self.can_shoot = True  # Add a flag to control shooting rate

    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        pressed_keys = pygame.key.get_pressed()

        # Rotation
        if pressed_keys[K_LEFT]:
            self.angle += 3
            self.rotate()
        if pressed_keys[K_RIGHT]:
            self.angle -= 3
            self.rotate()

        # Movement (forward/backward in direction of angle)
        if pressed_keys[K_UP]:
            self.move_forward(SCREEN_WIDTH, SCREEN_HEIGHT)
        if pressed_keys[K_DOWN]:
            self.move_backward(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Shooting
        if pressed_keys[K_SPACE] and self.can_shoot:  # Check the flag
            self.shoot()
            self.can_shoot = False  # Prevent shooting again until released

        if not pressed_keys[K_SPACE]: #Reset the flag when the space bar is released
            self.can_shoot = True

        # Update projectiles
        self.projectile_group.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    def shoot(self):
        # Calculate projectile starting position *outside* the player
        projectile_x = self.rect.centerx + (self.image.get_width() / 2 + 20) * math.cos(math.radians(self.angle))
        projectile_y = self.rect.centery - (self.image.get_height() / 2 + 20) * math.sin(math.radians(self.angle))
        projectile_position = (projectile_x, projectile_y)

        projectile = Projectile(projectile_position, self.angle)
        self.projectile_group.add(projectile)

    def move_forward(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # Calculate movement based on angle
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))

        self.rect.x += dx
        self.rect.y -= dy  # Subtract dy because pygame's y-axis is inverted

        # Keep player within screen bounds (optional, but recommended)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  #clamp_ip keeps the sprite within the rectangle

    def move_backward(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # Calculate movement based on angle (opposite direction)
        dx = -self.speed * math.cos(math.radians(self.angle))
        dy = -self.speed * math.sin(math.radians(self.angle))

        self.rect.x += dx
        self.rect.y -= dy  # Subtract dy because pygame's y-axis is inverted

        # Keep player within screen bounds (optional, but recommended)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.projectile_group.draw(surface) #Draw projectiles
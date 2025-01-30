import pygame
from pygame.locals import *
import math
from Projectile import Projectile
from Movement import Movement
from Globals import Globals

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.set_image("assets/PNG/Tanks/tankBlue.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.angle = 0
        self.speed = 3  
        self.projectile_group = pygame.sprite.Group()  # Group for projectiles
        self.can_shoot = True  # Flag to prevent rapid fire
        self.is_dead = False  # Flag to prevent movement and firing

        # Keep player within screen bounds 
        self.rect.clamp_ip(pygame.Rect(0, 0, Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))

    def set_image(self, image_path):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.original_image = pygame.transform.scale(self.original_image, (40, 40))
        self.image = self.original_image.copy()

    def update(self):
        if not self.is_dead:
            pressed_keys = pygame.key.get_pressed()

            # Shooting
            if pressed_keys[K_SPACE] and self.can_shoot:  # Check the flag
                self.shoot()
                self.can_shoot = False  # Prevent shooting again until released

            if not pressed_keys[K_SPACE]: #Reset the flag when the space bar is released
                self.can_shoot = True

            # Rotation
            if pressed_keys[K_a]:
                self.angle += 3
                self.rotate()
            if pressed_keys[K_d]:
                self.angle -= 3
                self.rotate()

            # Movement (forward/backward in direction of angle)
            if pressed_keys[K_w]:
                self.move_forward()
            if pressed_keys[K_s]:
                self.move_backward()

        # Update projectiles
        self.projectile_group.update()
        self.check_collisions()

    def move_forward(self):
        self.rect.x = Movement.calc_move_x(self.speed, self.angle, self.rect.x)
        self.rect.y = Movement.calc_move_y(self.speed, self.angle, self.rect.y)

    def move_backward(self):
        self.rect.x = Movement.calc_move_x(-self.speed, self.angle, self.rect.x)
        self.rect.y = Movement.calc_move_y(-self.speed, self.angle, self.rect.y)

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.projectile_group.draw(surface)

    def shoot(self):
        # Calculate projectile starting position outside the player
        projectile_position = Movement.calc_projectile_starting_point(
            self.rect.centerx, 
            self.rect.centery, 
            self.image.get_width(), 
            self.image.get_height(), 
            self.angle
        )

        self.projectile_group.add(
            Projectile(projectile_position, self.angle)
        )

    def check_collisions(self):
        for projectile in self.projectile_group:
            if pygame.sprite.collide_rect(projectile, self):  # Check for collision
                self.original_image = self.set_image("assets/PNG/Smoke/smokeGrey5.png")
                self.is_dead = True
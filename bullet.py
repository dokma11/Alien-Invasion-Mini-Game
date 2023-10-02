import pygame
from pygame.sprite import Sprite as Sp


class Bullet(Sp):
    def __init__(self, game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load('images/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (8, 18))
        self.rect = self.image.get_rect()

        # Setting bullets position
        self.rect.midtop = game.ship.rect.midtop

        # Store its position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Updating bullets position on the screen"""
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
       self.screen.blit(self.image, self.rect)

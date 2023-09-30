import pygame
from pygame.sprite import Sprite as Sp


class Ultimate(Sp):
    def __init__(self, game):
        """Create an ultimate ability object at the ship's current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Setting bullets position
        self.rect = pygame.Rect(0, 0, self.settings.ultimate_width, self.settings.ultimate_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store its position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Updating ultimates position on the screen"""
        self.y -= self.settings.ultimate_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_ultimate(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
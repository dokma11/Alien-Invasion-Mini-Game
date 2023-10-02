import pygame
from pygame.sprite import Sprite as Sp


class Ultimate(Sp):
    def __init__(self, game):
        """Create an ultimate ability object at the ship's current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load('images/ultimate-ability.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 50))
        self.rect = self.image.get_rect()

        # Setting bullets position
        self.rect.midtop = game.ship.rect.midtop

        # Store its position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Updating ultimates position on the screen"""
        self.y -= self.settings.ultimate_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_ultimate(self):
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()

        # Set aliens starting position (top of the screen)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the alien's exact horizontal position (making it more precise)
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Depending on the fleet direction, move the alien to the right or to the left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien image and set its rect attribute
        if game.stats.level == 1 or game.stats.level == 6 or game.stats.level == 11:
            self.image = pygame.image.load('images/alien-green.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect()
        elif game.stats.level == 2 or game.stats.level == 7 or game.stats.level == 12:
            self.image = pygame.image.load('images/alien-purple.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect()
        elif game.stats.level == 3 or game.stats.level == 8 or game.stats.level == 13:
            self.image = pygame.image.load('images/alien-pink.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect()
        elif game.stats.level == 4 or game.stats.level == 9 or game.stats.level == 14:
            self.image = pygame.image.load('images/alien-dark-blue.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load('images/alien-red.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
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

import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring info
        self.text_color = (34, 233, 80)

        # self.font = pygame.font.SysFont(None, 48)
        self.font = pygame.font.Font('images/pixel_font.ttf', 36)

        # Prepare the initial score image
        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_ships()
        self.prepare_ultimate_ability_message()

    def prepare_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render("Current Level: " + level_str, True, self.text_color)

        # Positioning the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prepare_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Display the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prepare_high_score()

    def prepare_ultimate_ability_message(self):
        self.ultimate_image = self.font.render("Ultimate ability ready!", True, self.text_color)

        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        # Display the score at the bottom right of the screen
        self.ultimate_rect = self.ultimate_image.get_rect()
        self.ultimate_rect.right = screen_width - 20  # Distance from the right edge
        self.ultimate_rect.bottom = screen_height - 20  # Distance from the bottom edge

    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

        # Display a message that the ultimate ability is ready
        if self.settings.ultimate_allowed:
            self.screen.blit(self.ultimate_image, self.ultimate_rect)

    def prepare_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
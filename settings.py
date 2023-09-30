import pygame


class Settings:
    def __init__(self):
        """Initialization of the games settings"""

        self.screen_info = pygame.display.Info()

        # Screen settings
        self.screen_width = self.screen_info.current_w + 70
        self.screen_height = self.screen_info.current_h + 50
        # Background color (in rgb values, should be gray)
        self.bg_color = (230, 230, 230)

        original_bg_image = pygame.image.load('images/background5(purple, pink - huge).bmp')

        # Resize the background image to fit the screen
        self.background_image = pygame.transform.scale(original_bg_image, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10

        # Ultimate ability settings
        self.ultimate_width = 140
        self.ultimate_height = 20
        self.ultimate_color = (255, 255, 255)

        # Alien settings
        self.fleet_vertical_speed = 6

        # How quickly the level speeds up
        self.speedup_scale = 1.1

        # How quickly the aliens value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 1 represents right, -1 represents left
        self.fleet_direction = 1

        self.ship_speed = 3.0
        self.bullet_speed = 4.5
        self.alien_speed = 1.0
        self.ultimate_speed = 3.5

        self.alien_points_worth = 50

        self.ultimate_allowed = False

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ultimate_speed *= self.speedup_scale

        self.alien_points_worth = int(self.alien_points_worth * self.score_scale)
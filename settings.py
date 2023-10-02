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
        original_bg_image_2 = pygame.image.load('images/background1(blue).bmp')
        original_bg_image_3 = pygame.image.load('images/background4(black-huge).bmp')

        # Resize the background image to fit the screen
        self.background_image_1 = pygame.transform.scale(original_bg_image, (self.screen_width, self.screen_height))
        self.background_image_2 = pygame.transform.scale(original_bg_image_2, (self.screen_width, self.screen_height))
        self.background_image_3 = pygame.transform.scale(original_bg_image_3, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullets_allowed = 10

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
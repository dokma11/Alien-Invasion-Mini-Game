class Settings:
    def __init__(self):
        """Initialization of the games settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        # Background color (in rgb values, should be gray)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

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

        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.alien_points_worth = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points_worth = int(self.alien_points_worth * self.score_scale)
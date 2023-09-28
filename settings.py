class Settings:
    def __init__(self):
        """Initialization of the games settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        # Background color (in rgb values, should be gray)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
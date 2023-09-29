import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage games behaviour and assets"""

    def __init__(self):
        """Initiate the game and start its resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self._create_fleet()

        self.game_active = False

        # Creating buttons
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            # User clicked on the QUIT button
            if event.type == pygame.QUIT:
                sys.exit()
            # User pressed a keyboard key
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # User released a keyboard key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # User pressed a mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_keydown_events(self, event):
        # Movement of the ship
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        # User fires a bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # User exits the game by pressing the 'Q' key
        elif event.key == pygame.K_q:
            sys.exit()
        # User start the game by pressing the 'P' key
        elif event.key == pygame.K_p:
            self.game_active = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_position):
        if self.play_button.rect.collidepoint(mouse_position) and not self.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.scoreboard.prepare_score()
            self.scoreboard.prepare_level()
            self.scoreboard.prepare_ships()
            self.game_active = True

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the cursor
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new = Bullet(self)
            self.bullets.add(new)

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        for b in self.bullets.sprites():
            b.draw_bullet()

        # Draw the ship
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # Draw the scoreboard
        self.scoreboard.display_score()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for b in self.bullets.copy():
            if b.rect.bottom <= 0:
                self.bullets.remove(b)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check if any bullets have hit aliens, if they have get rid of them
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points_worth * len(aliens)
            self.scoreboard.prepare_score()
            self.scoreboard.prepare_high_score()

        if not self.aliens:
            # Destroy the existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase the level
            self.stats.level += 1
            self.scoreboard.prepare_level()

    def _update_aliens(self):
        self._check_fleets_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom_edge()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prepare_ships()

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        # Create an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 15 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row so we reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        new_alien = Alien(self)
        new_alien.x = x
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)

    def _check_fleets_edges(self):
        for a in self.aliens.sprites():
            if a.check_edges():
                self._change_fleets_direction()
                break

    def _change_fleets_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_vertical_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom_edge(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


if __name__ == '__main__':
    """Make an instance of the game and run it"""
    a = AlienInvasion()
    a.run_game()

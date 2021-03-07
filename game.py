import pygame as pg
from settings import Settings
import game_functions as gf

from ship import Ship
from alien import Aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sound import Sound
from barrier import Barriers
from menu_screen import Button_title
from hs_button import hs_Button

import time


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")
        ship_image = pg.image.load('images/ship0.png')
        self.ship_height = ship_image.get_rect().height
        self.hs = 0
        self.finished = False
        self.sound = Sound(bg_music="sounds/ff7remakebattlemusic.wav")
        self.button_hs = self.aliens = self.stats = self.sb = self.ship = None
        self.button_title = self.aliens = self.stats = self.sb = self.ship = None
        self.sound.play()
        self.sound.pause_bg()
        self.play_button = self.aliens = self.stats = self.sb = self.ship = None
        self.restart()

    def restart(self):
        self.button_hs = hs_Button(settings=self.settings, screen=self.screen, msg="Highscores")
        self.button_title = Button_title(settings=self.settings, screen=self.screen, msg="Space Invasion")

        self.play_button = Button(settings=self.settings, screen=self.screen, msg="Play")
        self.stats = GameStats(settings=self.settings)
        self.sb = Scoreboard(game=self, sound=self.sound)
        self.settings.init_dynamic_settings()

        self.barriers = Barriers(game=self)
        self.aliens = Aliens(ship_height=self.ship_height, game=self, barriers=self.barriers)
        self.ship = Ship(aliens=self.aliens, sound=self.sound, game=self, barriers=self.barriers)
        self.aliens.add_ship(ship=self.ship)
        self.stats.high_score = self.hs
        self.sb.prep_high_score()

    def play(self):
        while not self.finished:
            gf.check_events(stats=self.stats, play_button=self.play_button, ship=self.ship, sound=self.sound,game=self,button_hs=self.button_hs)
            if self.stats.game_active:
                self.ship.update()
                self.aliens.update()
                self.barriers.update()

            self.screen.fill(self.settings.bg_color)
            self.ship.draw()
            self.aliens.draw()
            self.barriers.draw()
            self.sb.show_score()
            if not self.stats.game_active:
                self.button_title.draw()
                self.button_hs.draw()
                self.play_button.draw()
                self.sound.pause_bg()
            else:
                if not self.sound.playing_bg: self.sound.unpause_bg()
            pg.display.flip()

    def reset(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.aliens.create_fleet()
            self.ship.center_ship()
            time.sleep(0.5)
            self.ship.timer = Ship.timer
        else:
            self.stats.game_active = False
            self.sound.pause_bg()
            self.hs = self.stats.high_score
            self.restart()


def main():
    g = Game()
    g.play()
    print(f"High score was {g.stats.high_score}")
    with open("high_scores.txt", 'a') as f:
        f.write(f'High score was {g.stats.high_score}\n')
    # Vector.run_tests()
    # Quaternion.run_tests()
    # Matrix.run_tests()
    # Alien.run_tests()


if __name__ == '__main__':
    main()

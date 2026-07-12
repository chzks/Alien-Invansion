import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from score_board import Scoreboard



def run_game():
    """Инициализирует игру и создает обьект экрана."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    bg_image = pygame.image.load("converted_image.png")
    pygame.display.set_caption("Alien Invasion")
    stats = GameStatus(ai_settings)
    sb = Scoreboard(screen,ai_settings,stats)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    play_button = Button(ai_settings,screen,"play")

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        gf.update_screen(ai_settings, bg_image, screen, stats,sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,bullets)
            ship.update()


run_game()
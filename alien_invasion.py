import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """Инициализирует игру и создает обьект экрана."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    bg_image = pygame.image.load("converted_image.png")
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,bg_image, screen, ship,aliens,bullets)

run_game()

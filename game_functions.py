import sys
import pygame

from alien import Alien
from bullet import Bullet


def check_keydown_event(event,ai_settings,screen,ship,bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event,ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

def fire_bullets(ai_settings,screen,ship,bullets):
    """Выпускает пулю, если максимум еще не достигнут."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_events(ai_settings,screen,ship,bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)


def update_screen(ai_settings,bg_image, screen, ship,aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.blit(bg_image, (0, 0))
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(ai_settings,alien_width):
    """Вычисляет колличество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - (alien_width * 2)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings,screen,aliens):
    """Создает флот пришельцев."""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

    for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number)

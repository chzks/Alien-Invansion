import sys
import pygame

from bullet import Bullet


def check_keydown_event(event,ai_settings,screen,ship,bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)


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


def update_screen(ai_settings,bg_image, screen, ship, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.blit(bg_image, (0, 0))
    ship.blitme()
    for bullet in bullets:
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)



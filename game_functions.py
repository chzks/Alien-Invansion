import sys
import pygame
from alien import Alien
from bullet import Bullet
from time import sleep


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


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            check_play_button_event(ai_settings, screen, stats, play_button, ship, aliens,bullets, mouse_x,mouse_y)

def check_play_button_event(ai_settings, screen, stats, play_button, ship, aliens,bullets, mouse_x,mouse_y):
    """Запускает новую игру при нажатии кнопки Play Button."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_status()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_settings,bg_image, screen,stats,sb, ship, aliens, bullets,play_button):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.blit(bg_image, (0, 0))
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if stats.game_active == False:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_allien_colisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_allien_colisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Обработка коллизий пуль с пришельцами."""
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
    sb.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
    """Вычисляет колличество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - (alien_width * 2)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет колличество рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """Создает флот пришельцев."""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)


def check_fleet_edges(ai_settings,aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """Опускает весь флот и меняет его направление."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """Обрабатывает столкновение корабля с пришельцем."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """Проверяет, добрались ли пришельцы до нижнего края экрана."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


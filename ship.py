import pygame
from settings import Settings
class Ship():

    def __init__(self,screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = Settings()

        self.image = pygame.image.load("main_korabl.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 10



    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль по центру нижней стороны."""
        self.centerx = self.screen_rect.centerx

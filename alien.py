import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Alien(sprite.Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self,ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('korabl_vrag.png')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image,self.rect)
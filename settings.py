class Settings():
    """Класс для сохранения всех настроек Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1200
        self.screen_height = 840
        self.bullet_speed_factor = 15
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

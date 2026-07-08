class Settings():
    """Класс для сохранения всех настроек Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bullet_speed_factor = 15
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 45
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.bg_color = None

    def initialize_dynamic_settings(self):
        """Инициализация настроек, изменяющихся в ходе игры."""
        self.alien_points = 50
        self.alien_speed_factor = 4
        self.bullet_speed_factor = 6
        self.ship_speed_factor = 1.5
        self.score_scale = 1.5
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки стоимости и скорости пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)

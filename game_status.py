class GameStatus():
    """Отслеживание статистики игры Alien Invasion."""

    def __init__(self,ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_status()
        self.game_active = False

    def reset_status(self):
        """Инициализирует статистику, меняющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

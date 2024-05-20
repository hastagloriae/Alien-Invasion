class GameStats:
    """Відстежувати статистику гри"""

    def __init__(self, ai_game):
        """Інаціалізація статистики."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Розпочати гру в активному стані
        self.game_active = True

    def reset_stats(self):
        """Ініціалізувати статистики, зо сможе змінювати впровдовж гри"""
        self.ships_left = self.settings.ship_limit


class Settings:
    """Клас для збереження налаштування всіх ігри"""

    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self. bg_color = (230, 230, 230)

        # Налаштування корабля
        self.ship_speed = 3.5
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_speed = 4.0
        self.bullet_widht = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Налаштування прибульця.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1 праворуч -1 ліворуч
        self.fleet_direction = 1
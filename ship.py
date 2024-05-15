import pygame

class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його позицію.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Стоврит кожен новий корабль внизу єкрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Намалювати корабль у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)
import pygame

class Alien:
    """Клас для створення прибульця"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його позицію.
        self.image = pygame.image.load('images/pixel.png')
        self.rect = self.image.get_rect()

        # Стоврит кожен новий корабль внизу єкрана, по центру
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Намалювати корабль у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)
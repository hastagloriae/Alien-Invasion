import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з фото"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантажте чуже зображення і встановіть його атрибут rect.
        self.image = pygame.image.load('images/pixel.png')
        self.rect = self.image.get_rect()

        # Запускайте кожного нового прибульця у верхньому лівому кутку екрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Зберігайте точне горизонтальне положення інопланетянина
        self.x = float(self.rect.x)

    def check_edges(self):
        """Повертає істину, якщо прибулецб знаходиться на краю екрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Змістити прибульця правуруч чи ліворуч"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
# Python 3.0
# Bartosz Wolak
# created 23.07.2021
# updated 23.07.2021
"""
Module responible for keeping data for buttons,dependent on pygame
"""

import pygame
import src.Drawable
import src.loading


class Button(pygame.sprite.Sprite):
    def __init__(self, pos: (int, int), label: str, size: (int, int) = (200, 50)):
        pygame.sprite.Sprite.__init__(self)

        self.label = label
        self.rect = pygame.Rect(pos, size)

        self.static_image = pygame.Surface(size)
        self.static_image.fill(src.loading.colours['light_gray'])

        self.hover_image = pygame.Surface(size)
        self.hover_image.fill(src.loading.colours['dark_gray'])

        self.image = pygame.Surface(size)
        self.image.blit(self.static_image, (0, 0))

        self.font = pygame.font.SysFont('Corbel', 25)
        self.pygame_rendered_label = self.font.render(self.label, True, src.loading.colours['font_colour'])

        self.image.blit(self.pygame_rendered_label, (self.rect.width / 2 - 5 * len(self.label), self.rect.height / 2 - 15))
        self.hover_image.blit(self.pygame_rendered_label, (self.rect.width / 2 - 5 * len(self.label), self.rect.height / 2 - 15))
        self.static_image.blit(self.pygame_rendered_label, (self.rect.width / 2 - 5 * len(self.label), self.rect.height / 2 - 15))

        self.state = 'static'
        self.function = None

    def hover(self):
        if self.state == 'static':
            self.image.blit(self.hover_image, (0, 0))
            self.state = 'hover'

    def static(self):
        if self.state == 'hover':
            self.image.blit(self.static_image, (0, 0))
            self.state = 'static'

    def bind(self, func):
        self.function = func

    def trigger(self):
        self.function()

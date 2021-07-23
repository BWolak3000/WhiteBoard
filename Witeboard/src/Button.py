# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 22.07.2021
"""
Module responible for keeping data for buttons,dependent on pygame
"""

import pygame
import src.Drawable
import src.loading


class Button():
    def __init__(self, pos: (int, int), label: str, size: (int, int) = (200, 50)):
        # pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        # self.image, self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.label = label
        self.x, self.y = pos
        self.length, self.height = size
        self.func = None
        self.font = pygame.font.SysFont('Corbel', 25)
        self.colours = {
            'black': (0, 0, 0),
            'light_gray': (170, 170, 170),
            'dark_gray': (100, 100, 100),
            'white': (255, 255, 255),
            'font_colour': (255, 255, 255)
        }
        self.pygame_rendered_label = self.font.render(self.label, True, self.colours['font_colour'])

    def if_contains(self, target: (int, int)):
        if self.x <= target[0] <= self.x + self.length and self.y <= target[1] <= self.y + self.height:
            return True
        else:
            return False

    def draw(self, screen, mode):
        pygame.draw.rect(screen, self.colours[mode], [self.x, self.y, self.length, self.height])
        screen.blit(self.pygame_rendered_label, (self.length / 2 + self.x - 5 * len(self.label), self.height / 2 + self.y - 10))

    def bind(self, func):
        self.func = func

    def trigger(self):
        self.func()


def print_123():
    print(123)


if __name__ == '__main__':
    b = Button((0, 0), 'button')
    print('should be True:')
    print(b.if_contains((10, 10)))
    print('should be False:')
    print(b.if_contains((10, 1000)))
    print('should be 123:')
    b.bind(print_123)
    b.trigger()



# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 22.07.2021

import pygame


class Drawable(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()

    def draw(self, screen):
        raise NotImplementedError()

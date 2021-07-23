# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 22.07.2021

import pygame
import src.Drawable


class Actor(src.Drawable):
    def __init__(self, pos: (int, int), name: str, size: (int, int) = (50, 50)):
        self.name = name
        self.x, self.y = pos
        self.length, self.height = size
        self.image = None

    def bind_image(self, image):
        self.image = image

    def draw(self):
        pass

# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 23.07.2021
"""
Module responible for main functions of app
"""

import pygame
import os
import src.GUI


all_sprites = pygame.sprite.RenderPlain()


class WhiteBoardApp:
    def __init__(self):
        pygame.init()
        self.res = (1220, 720)

        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption('white board')

        self.GUI = src.GUI.MyGUI(self.res)

        all_sprites.add(self.GUI)

    def update(self):
        self.GUI.update()

        all_sprites.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    print('this file does nothing')

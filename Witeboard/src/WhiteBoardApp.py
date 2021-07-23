# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 22.07.2021
"""
Module responible for main functions of app
"""

import pygame
import os
import src.Button
import src.ButtonInConstruction

color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)


def quit_my_program():
    pygame.quit()
    exit(0)


class WhiteBoardApp:
    def __init__(self):
        pygame.init()
        self.res = (720, 720)

        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption('white board')
        self.screen.fill((50, 50, 50))

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        quit_button = src.ButtonInConstruction.Button((10, 10), 'quit', (50, 50))
        # quit_button.bind(quit_my_program)

        self.buttons = {
            'exit_button': quit_button
        }

        self.allsprites = pygame.sprite.RenderPlain(quit_button)

    def update(self):
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons.values():
                    if button.rect.collidepoint(mouse):
                        # button.trigger()
                        print('collided')

        self.screen.fill((50, 50, 50))

        for button in self.buttons.values():
            if button.rect.collidepoint(mouse):
                button.hover()
            else:
                button.static()
        self.allsprites.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    a = WhiteBoardApp()

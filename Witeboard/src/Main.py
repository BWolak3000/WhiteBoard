# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 23.07.2021
"""
Module responible for starting app and main loop
"""
import os
import src.WhiteBoardApp
import pygame

going = True


def main():
    app = src.WhiteBoardApp.WhiteBoardApp()
    clock = pygame.time.Clock()

    while going:
        clock.tick(60)
        app.update()


if __name__ == '__main__':
    main()

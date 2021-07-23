# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 22.07.2021
"""
Module responible for starting app and main loop
"""
import os
import pygame
import src.WhiteBoardApp

going = True


def main():
    app = src.WhiteBoardApp.WhiteBoardApp()
    while going:
        app.update()


if __name__ == '__main__':
    main()

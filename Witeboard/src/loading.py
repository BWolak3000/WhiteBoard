# Python 3.0
# Bartosz Wolak
# created 23.07.2021
# updated 23.07.2021
import pygame
import os


main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, 'assets')

colours = {
            'black': (0, 0, 0),
            'light_gray': (170, 170, 170),
            'dark_gray': (100, 100, 100),
            'white': (255, 255, 255),
            'font_colour': (255, 255, 255),
            'light_light_gray': (50, 50, 50)
        }


#functions to create our resources
def load_image(name):
    fullname = os.path.join(assets_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit()
    image = image.convert()
    return image, image.get_rect()
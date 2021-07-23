# Python 3.0
# Bartosz Wolak
# created 22.07.2021
# updated 23.07.2021


import pygame
import os
import src.Button
import src.loading
import src.exit


class MyGUI(pygame.sprite.Sprite):
    def __init__(self, screen_res):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect((0, 0), screen_res)

        self.background = pygame.Surface(screen_res)
        self.background.fill(src.loading.colours['light_light_gray'])

        self.panel = pygame.Surface((screen_res[0] - 200 - 20, screen_res[1] - 20))
        self.panel.fill(src.loading.colours['white'])

        self.buttons = {}

        quit_button = src.Button.Button((10, 10), 'quit', (50, 50))
        quit_button.bind(src.exit.quit_my_program)

        self.number_of_buttons_created = 0
        self.waiting_list = []
        create_button_button = src.Button.Button((70, 10), 'create', (70, 50))
        create_button_button.bind(self.add_button)

        self.buttons['exit_button'] = quit_button
        self.buttons['create_button_button'] = create_button_button

        self.image = pygame.Surface(screen_res)
        self.image.fill(src.loading.colours['light_light_gray'])

        self.blit_all_to_self_image()

    def update(self):
        for button in self.waiting_list:
            self.buttons['new_button_' + str(self.number_of_buttons_created)] = button
            self.number_of_buttons_created += 1

        self.waiting_list.clear()

        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                src.exit.quit_my_program()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons.values():
                    if button.rect.collidepoint(mouse):
                        button.trigger()

        for button in self.buttons.values():
            if button.rect.collidepoint(mouse):
                button.hover()
            else:
                button.static()

        self.blit_all_to_self_image()

    def blit_all_to_self_image(self):

        self.image.blit(self.background, (0, 0))
        self.image.blit(self.panel, (210, 10))

        for button in self.buttons.values():
            self.image.blit(button.image, (button.rect.left, button.rect.top))

    def add_button(self):
        pos, label, size, func = ((10, self.number_of_buttons_created * 60 + 70), 'new button',
                                  (190, 50), src.exit.nothing)
        new_button = src.Button.Button(pos, label, size)
        new_button.bind(func)

        self.waiting_list.append(new_button)

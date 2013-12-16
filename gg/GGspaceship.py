'''
Created on 8 Dec 2013

@author: tore
'''
import os.path

import pygame.image


class SpaceShip(object):

    def __init__(self):

        ssimgpath = os.path.join(".", "gg", "data", "gfx", "ss1.bmp")

        self.oxygen = 100
        self.hull = 0
        self.img = pygame.image.load(ssimgpath).convert()
        self.rect = self.img.get_rect()
        self.x = 0
        self.y = 0

    def eventtest(self, uevent):

        self.uevent = uevent

    def move(self):

        if self.uevent.w == True:

            print('test')

            self.y -= 1

            # self.rect = self.rect.move(0, -1)

        if self.uevent.a == True:

            self.x -= 1

            # self.rect = self.rect.move(-1, 0)

        if self.uevent.s == True:

            self.y += 1

            # self.rect = self.rect.move(0, 1)

        if self.uevent.d == True:

            self.x += 1

            # self.rect = self.rect.move(1, 0)

    def render(self, background):

        # self.img = pygame.transform.rotozoom(self.img, 0, 1)
        # objects.ssrect = objects.ssimg.get_rect()
        self.img.set_colorkey((255, 0, 255))
        background.blit(self.img, self.rect)

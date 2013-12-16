'''
Created on 8 Dec 2013

@author: tore
'''
import os.path

import pygame.image

from gg.GGgridobject import GridObject


class SpaceShip(GridObject):

    def __init__(self):

        super(GridObject, self).__init__()

        ssimgpath = os.path.join(".", "gg", "data", "gfx", "ss1.bmp")

        self.x = 0
        self.y = 0

        self.oxygen = 100
        self.hull = 0
        self.img = pygame.image.load(ssimgpath).convert()
        self.rect = self.img.get_rect()

    def eventtest(self, uevent):

        self.uevent = uevent

    def move(self):

        if self.uevent.w == True:

            print('test')

            self.y = self.y - 1

            # self.rect = self.rect.move(0, -1)

        if self.uevent.a == True:

            self.x = self.x - 1

            # self.rect = self.rect.move(-1, 0)

        if self.uevent.s == True:

            self.y = self.y + 1

            # self.rect = self.rect.move(0, 1)

        if self.uevent.d == True:

            self.x = self.x + 1

            # self.rect = self.rect.move(1, 0)

'''
Created on 8 Dec 2013

@author: tore
'''
import pygame.image


class SpaceShip(object):

    def __init__(self):

        self.oxygen = 100
        self.hull = 0
        self.ssimg = pygame.image.load("./gg/data/gfx/ss1.bmp").convert()
        self.ssrect = self.ssimg.get_rect()
        self.x = 0
        self.y = 0

    def eventtest(self, uevent):

        self.uevent = uevent

    def move(self):

        if self.uevent.w == True:

            print('test')

            self.ssrect = self.ssrect.move(0, -1)

        elif self.uevent.a == True:

            self.ssrect = self.ssrect.move(-1, 0)

        elif self.uevent.s == True:

            self.ssrect = self.ssrect.move(0, 1)

        elif self.uevent.d == True:

            self.ssrect = self.ssrect.move(1, 0)

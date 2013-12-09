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

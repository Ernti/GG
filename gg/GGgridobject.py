'''
Created on 16 Dec 2013

@author: tore
'''
import pygame


class GridObject:

    def __init__(self):

        self.rect = pygame.rect
        self.img = pygame.image

    def render(self, background):

        # self.img = pygame.transform.rotozoom(self.img, 0, 1)
        # objects.ssrect = objects.ssimg.get_rect()
        self.img.set_colorkey((255, 0, 255))
        background.blit(self.img, self.rect)

'''
Created on 9 Dec 2013

@author: tore
'''

import pygame


class Render(object):

    def __init__(self):

        self.size = self.width, self.height = 1280, 720
        self.black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)

        self.font = pygame.font.Font(None, 36)

    def render(self, oxygen):

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.black)

        self.text = self.font.render("Oxygen: " + oxygen, 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos = self.background.get_rect()
        self.background.blit(self.text, self.textpos)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

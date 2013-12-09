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
        pygame.display.set_caption('GG')

        self.font = pygame.font.Font(None, 36)

        self.fullscreen = False

    def render(self, oxygen, fps):

        self.background = pygame.Surface(self.size)
        self.background = self.background.convert()
        self.background.fill(self.black)

        self.text = self.font.render("Oxygen: " + oxygen, 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos = self.background.get_rect()
        self.background.blit(self.text, self.textpos)

        self.text2 = self.font.render("fps: " + fps, 1, (255, 255, 255))
        self.text2pos = self.text2.get_rect()
        self.text2pos.centerx = self.background.get_rect().centerx
        self.background.blit(self.text2, self.text2pos)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

'''
Created on 9 Dec 2013

@author: tore
'''

import os.path

import pygame


class Render(object):

    def __init__(self):

        self.size = self.width, self.height = 1280, 720
        self.black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.screen.set_colorkey((255, 0, 255))
        pygame.display.set_caption('GG')

        fontpath = os.path.join(".", "gg", "data", "fonts", "arial.ttf")
        self.font = pygame.font.Font(fontpath, 36)

        self.fullscreen = False
        self.fsres = (1920, 1080)

    def render(self, oxygen, fps, sg):

        self.background = pygame.Surface(self.size)
        self.background = self.background.convert()
        self.background.fill(self.black)

        for objects in sg.go.objects:

            ssimg = pygame.transform.rotozoom(objects.ssimg, 0, sg.z)
            # objects.ssrect = objects.ssimg.get_rect()
            ssimg.set_colorkey((255, 0, 255))
            self.background.blit(ssimg, objects.ssrect)

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

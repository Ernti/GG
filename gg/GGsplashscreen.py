'''
Created on 10 May 2014

@author: tore
'''
import os
import pygame


class SplashScreen(object):

    def __init__(self):

        self.splashscreen = pygame.display.set_mode((600, 400), pygame.NOFRAME)

        imgpath = os.path.join(".", "gg", "data", "gfx", "splashscreen.png")
        self.splashimg = pygame.image.load(imgpath).convert()

        self.background = pygame.Surface((600, 400))
        self.background = self.background.convert()
        self.background.fill((200, 200, 200))
        self.background.blit(self.splashimg, (0, 0))
        self.splashscreen.blit(self.background, (0, 0))
        pygame.display.flip()
        pygame.time.wait(10)
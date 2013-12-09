'''
Created on 9 Dec 2013

@author: tore
'''
import sys

import pygame.event


class UserEvents(object):

    def __init__(self):

        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.lmsbtn = False
        self.rmsbtn = False


class Events(object):

    def __init__(self, ss, render):

        self.uevents = UserEvents()
        self.ss = ss
        self.render = render

    def eventLoop(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_o:
                    self.ss.oxygen = self.ss.oxygen - 1

                elif event.key == pygame.K_F11:

                    if self.render.fullscreen == True:
                        self.render.fullscreen = False
                        self.render.screen = pygame.display. \
                        set_mode(self.render.size,
                                pygame.RESIZABLE)

                    else:
                        self.render.fullscreen = True
                        self.render.screen = pygame.display. \
                        set_mode(self.render.fsres,
                                pygame.FULLSCREEN |
                                pygame.HWSURFACE |
                                pygame.DOUBLEBUF)

                elif event.key == pygame.K_w:
                    self.uevents.w = True

                elif event.key == pygame.K_a:
                    self.uevents.a = True

                elif event.key == pygame.K_s:
                    self.uevents.s = True

                elif event.key == pygame.K_d:
                    self.uevents.d = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    self.uevents.w = False

                elif event.key == pygame.K_a:
                    self.uevents.a = False

                elif event.key == pygame.K_s:
                    self.uevents.s = False

                elif event.key == pygame.K_d:
                    self.uevents.d = False

            elif event.type == pygame.VIDEORESIZE:
                self.ss.oxygen = event.w

                if(event.w > 640):
                    self.render.size = (event.w, int(event.w / 16 * 9))
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)

                else:
                    self.render.size = (640, 360)
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)

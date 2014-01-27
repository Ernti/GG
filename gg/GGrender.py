'''
Created on 9 Dec 2013

@author: tore
'''
import ctypes

import pygame
from OpenGL.GL import glClear, glClearColor, glMatrixMode, GL_PROJECTION, \
                        GL_MODELVIEW, glLoadIdentity, GL_COLOR_BUFFER_BIT, \
                        GL_DEPTH_BUFFER_BIT
from OpenGL.GLU import gluPerspective, gluLookAt


class Render(object):

    def __init__(self, ggci):

        self.ggci = ggci

        self.black = 0.0, 0.0, 0.0, 1.0

        self.screen = pygame.display.set_mode(self.ggci.ggdata.screensize,
                                              pygame.DOUBLEBUF |
                                              pygame.OPENGL |
                                              pygame.HWPALETTE |
                                              pygame.HWSURFACE,
                                              24)

        glClearColor(0.0, 0.0, 0.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1.0 * self.ggci.ggdata.screenwidth
                       / self.ggci.ggdata.screenheight, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

        pygame.display.set_caption('GG')

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for objects in self.ggci.objectlist.objectlist:

            objects.render()

        pygame.display.flip()

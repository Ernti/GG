'''
Created on 9 Dec 2013

@author: tore
'''

import pygame
from OpenGL.GL import glClear, glClearColor, glMatrixMode, GL_PROJECTION, \
                         GL_MODELVIEW, glLoadIdentity, GL_COLOR_BUFFER_BIT, \
                         GL_DEPTH_BUFFER_BIT
from OpenGL.GLU import gluPerspective, gluLookAt


class Render(object):

    def __init__(self, ggci):

        self.ggci = ggci

        self.size = self.width, self.height = 1280, 720
        self.black = 0.0, 0.0, 0.0, 1.0

        self.screen = pygame.display.set_mode(self.size,
                                              pygame.OPENGL | pygame.DOUBLEBUF,
                                              24)

        glClearColor(0.0, 0.0, 0.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1.0 * self.width / self.height, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

#        self.screen.set_colorkey((255, 0, 255))
        pygame.display.set_caption('GG')
#
#        fontpath = os.path.join(".", "gg", "data", "fonts", "arial.ttf")
#        self.font = pygame.font.Font(fontpath, 36)
#
#        self.fullscreen = False
#        self.fsres = (1920, 1080)

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for objects in self.ggci.objectlist.objectlist:

            objects.render()

        pygame.display.flip()

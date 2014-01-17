'''
Created on 9 Dec 2013

@author: tore
'''

import os.path

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *


class Render(object):

    def __init__(self, ggci):

        self.ggci = ggci

        self.size = self.width, self.height = 1280, 720
        self.black = 0.0, 0.0, 0.0, 1.0

        self.screen = pygame.display.set_mode(self.size, pygame.OPENGL, 16)

        glClearColor(0.0, 0.0, 0.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(60, 1.0 * self.width / self.height, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, -10, 10, 0, 0, 0, 0, 1, 0)

#        self.screen.set_colorkey((255, 0, 255))
        pygame.display.set_caption('GG')
#
#        fontpath = os.path.join(".", "gg", "data", "fonts", "arial.ttf")
#        self.font = pygame.font.Font(fontpath, 36)
#
#        self.fullscreen = False
#        self.fsres = (1920, 1080)

    def render(self, oxygen, fps, sg, player):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # print(fps)


        glTranslatef(0, 0, 0)
        [glBegin(GL_TRIANGLES),
            glColor(255, 0, 0), glVertex3f(-4, 4, 0),
            glColor(0, 255, 0), glVertex3f(4, 4, 0),
            glColor(0, 0, 255), glVertex3f(0, -4, 0),
        glEnd()]

        pygame.display.flip()

#        self.background = pygame.Surface(self.size)
#        self.background = self.background.convert()
#        self.background.fill(self.black)

#        for objects in self.ggci.objectlist.objectlist:

#            objects.render(self.background, player)
#            print('rendered')
#            print('rect.x ', objects.rect.x)
#            print(player.x)

            # ssimg = pygame.transform.rotozoom(objects.ssimg, 0, sg.z)
            # objects.ssrect = objects.ssimg.get_rect()
            # ssimg.set_colorkey((255, 0, 255))
            # self.background.blit(ssimg, objects.ssrect)

#        self.text = self.font.render("Oxygen: " + oxygen, 1, (255, 255, 255))
#        self.textpos = self.text.get_rect()
#        self.textpos = self.background.get_rect()
#        self.background.blit(self.text, self.textpos)

#        self.text2 = self.font.render("fps: " + fps, 1, (255, 255, 255))
#        self.text2pos = self.text2.get_rect()
#        self.text2pos.centerx = self.background.get_rect().centerx
#        self.background.blit(self.text2, self.text2pos)

#        self.screen.blit(self.background, (0, 0))
#        pygame.display.flip()

        # testing

        # pygame.display.update(self.ggci.objectlist.updatelist)

    def drawText(self, position, textString):
        font = pygame.font.Font (None, 64)
        textSurface = font.render(textString, True, (0, 0, 0, 255), (0, 0, 0, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos3d(*position)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

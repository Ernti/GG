'''
Created on 9 Dec 2013

@author: tore
'''
import ctypes
import os.path
from OpenGL.constants import GL_UNSIGNED_BYTE

import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
import sys


class Render(object):

    def __init__(self, ggci):

        self.ggci = ggci

        self.black = 0.0, 0.0, 0.0, 1.0

        self.screen = pygame.display.set_mode(self.ggci.ggdata.screensize,
                                              pygame.DOUBLEBUF |
                                              pygame.OPENGL,
                                              24)

        #glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
        #glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        #glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        #glEnable(GL_LIGHT0)
        #glEnable(GL_LIGHTING)
        #glEnable(GL_COLOR_MATERIAL)
        #glEnable(GL_DEPTH_TEST)
        #glShadeModel(GL_SMOOTH)

        glClearColor(0.0, 0.0, 0.0, 1.0)

        pygame.display.set_caption('GG')

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        self.resize(self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glPushMatrix()

        for objects in self.ggci.objectlist.objectlist:

            objects.render()

        # glCallList(self.ggci.obj.gl_list)

        glPopMatrix()

        self.ggci.textrender.textView()
        glPushMatrix()

        for objects in self.ggci.objectlist.objectlist:

            objects.renderNameplate()

        self.ggci.textrender.print(str(self.ggci.speed) + " km/h", self.ggci.textrender.char2,
                                   self.ggci.ggdata.screenwidth - 200, 10)
        line = 0
        while line < self.ggci.ggdata.chatlength:
            if line < len(self.ggci.chat.chat):
                self.ggci.textrender.print(self.ggci.chat.chat[(len(self.ggci.chat.chat) - line) - 1],
                                           self.ggci.textrender.char, 10, 20 * (line + 1))
            line += 1

        #if self.ggci.chat.input is True:
        #   self.print(self.ggci.chat.inputstring, self.char, 10, 20)

        #for line in self.ggci.chat.chat:
        #    if len(self.ggci.chat.chat) - self.ggci.chat.chat.index(line) < 5:
        #        self.print(line, self.char, 10,
        #                    20 * len(self.ggci.chat.chat) - 20 * self.ggci.chat.chat.index(line))
        glPopMatrix()

        pygame.display.flip()

    def resize(self, w, h):
        if h == 0: h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(w) / float(h), 0.1, 1000.0)
        #glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

'''
Created on 9 Dec 2013

@author: tore
'''

import math
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
        glEnable(GL_POINT_SMOOTH)
        glPointSize(3.0)

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

        r=1.0
        angle=0
        glBegin(GL_POLYGON)
        while angle < 2 * math.pi:
            glColor3f(0, 0, 0)
            glVertex3f(6 + r * math.cos(angle), 3 + r * math.sin(angle), 0)
            angle += 0.1
        glEnd()

        r=1.0
        angle=0
        glBegin(GL_LINE_LOOP)
        while angle < 2 * math.pi:
            glColor3f(0.5, 0.5, 0.5)
            glVertex3f(6 + r * math.cos(angle), 3 + r * math.sin(angle), 0)
            angle += 0.1
        glEnd()

        for objects in self.ggci.objectlist.objectlist:

            if objects.id is -1:
                glBegin(GL_POINTS)
                glColor(0, 1, 0)
                glVertex3f(6 + (objects.x - self.ggci.player.playership.x)/100, 3 + (objects.y - self.ggci.player.playership.y)/100, 0)
                glEnd()
            elif  math.sqrt(((objects.x - self.ggci.player.playership.x)/100)**2 + ((objects.y - self.ggci.player.playership.y)/100) ** 2) < 1:
                glBegin(GL_POINTS)
                glColor(1, 0, 0)
                glVertex3f(6 + (objects.x - self.ggci.player.playership.x)/100, 3 + (objects.y - self.ggci.player.playership.y)/100, 0)
                glEnd()

        glPopMatrix()

        self.ggci.textrender.textView()
        glPushMatrix()

        for objects in self.ggci.objectlist.objectlist:

            if objects.id is not -1:

                objects.renderNameplate()

        self.ggci.textrender.print(str(self.ggci.speed) + " km/h", self.ggci.textrender.char2,
                                   self.ggci.ggdata.screenwidth - 200, 10, "left")
        line = 0
        while line < self.ggci.ggdata.chatlength:
            if line < len(self.ggci.chat.chat):
                self.ggci.textrender.print(self.ggci.chat.chat[(len(self.ggci.chat.chat) - line) - 1],
                                           self.ggci.textrender.char, 10, 20 * (line + 1), "left")
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

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

        pygame.font.init()

        if not pygame.font.get_init():
            print('Could not render font.')
            sys.exit(0)
        self.font = pygame.font.Font(os.path.join(".", "gg", "data", "fonts", "arial.ttf"), 18)
        self.char = []
        for c in range(256):
            self.char.append(self.createCharacter(chr(c)))
        self.char = tuple(self.char)
        self.lw = self.char[ord('0')][1]
        self.lh = self.char[ord('0')][2]
        self.angle = 0.0
        self.font = pygame.font.Font(os.path.join(".", "gg", "data", "fonts", "arial.ttf"), 50)
        self.char2 = []
        for c in range(256):
            self.char2.append(self.createCharacter(chr(c)))
        self.char2 = tuple(self.char2)
        self.lw2 = self.char2[ord('0')][1]
        self.lh2 = self.char2[ord('0')][2]
        self.angle2 = 0.0

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        self.resize(self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glPushMatrix()

        for objects in self.ggci.objectlist.objectlist:

            objects.render()

        # glCallList(self.ggci.obj.gl_list)

        glPopMatrix()

        self.textView()
        glPushMatrix()
        self.print(str(self.ggci.speed) + " km/h", self.char2, self.ggci.ggdata.screenwidth - 200, 10)
        for line in self.ggci.chat:
            self.print(self.ggci.chat[self.ggci.chat.index(line)],
                       self.char, 10,
                       20 * len(self.ggci.chat) - 20 * self.ggci.chat.index(line))
        glPopMatrix()

        pygame.display.flip()

    def print(self, s, char, x, y):
        s = str(s)
        i = 0
        lx = 0
        length = len(s)
        while i < length:
            glRasterPos2i(x + lx, y)
            ch = char[ord(s[i])]
            glDrawPixels(ch[1], ch[2], GL_RGBA, GL_UNSIGNED_BYTE, ch[0])
            lx += ch[1]
            i += 1

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

    def textView(self):
        glViewport(0, 0, self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.ggci.ggdata.screenwidth - 1.0, 0.0, self.ggci.ggdata.screenheight - 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def createCharacter(self, s):
        try:
            letter_render = self.font.render(s, 1, (255, 255, 255), (0, 0, 0))
            letter = pygame.image.tostring(letter_render, 'RGBA', 1)
            letter_w, letter_h = letter_render.get_size()

        except:
            letter = None
            letter_w = 0
            letter_h = 0
        return letter, letter_w, letter_h

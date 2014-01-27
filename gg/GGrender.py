'''
Created on 9 Dec 2013

@author: tore
'''
import ctypes
import os.path
from OpenGL.constants import GL_UNSIGNED_BYTE

import pygame
from OpenGL.GL import glClear, glClearColor, glMatrixMode, GL_PROJECTION, \
                        GL_MODELVIEW, glLoadIdentity, GL_COLOR_BUFFER_BIT, \
                        GL_DEPTH_BUFFER_BIT, glOrtho, glPushMatrix, \
                        glPopMatrix, glRasterPos2i, glDrawPixels, GL_RGBA, \
                        glViewport
from OpenGL.GLU import gluPerspective, gluLookAt
import sys


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

        pygame.display.set_caption('GG')

        pygame.font.init()

        if not pygame.font.get_init():
            print('Could not render font.')
            sys.exit(0)
        self.font = pygame.font.Font(os.path.join(".","gg","data","fonts","arial.ttf"), 18)
        self.char = []
        for c in range(256):
            self.char.append(self.CreateCharacter(chr(c)))
        self.char = tuple(self.char)
        self.lw = self.char[ord('0')][1]
        self.lh = self.char[ord('0')][2]
        self.angle = 0.0

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        self.resize(self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glPushMatrix()

        for objects in self.ggci.objectlist.objectlist:

            objects.render()

        glPopMatrix()

        self.Print(str(self.ggci.speed) + " km/h", 10, self.ggci.ggdata.screenheight - 26)

        pygame.display.flip()

    def Print(self,s,x,y):
        s = str(s)
        i = 0
        lx = 0
        length = len(s)
        self.textView()
        glPushMatrix()
        while i < length:
            glRasterPos2i(x + lx, y)
            ch = self.char[ ord( s[i] ) ]
            glDrawPixels(ch[1], ch[2], GL_RGBA, GL_UNSIGNED_BYTE, ch[0])
            lx += ch[1]
            i += 1
        glPopMatrix()

    def resize(self,w,h):
        if h == 0: h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(w) / float(h), 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

    def textView(self):
        glViewport(0,0,self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.ggci.ggdata.screenwidth - 1.0, 0.0, self.ggci.ggdata.screenheight - 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def CreateCharacter(self, s):
        try:
            letter_render = self.font.render(s, 1, (255,255,255), (0,0,0))
            letter = pygame.image.tostring(letter_render, 'RGBA', 1)
            letter_w, letter_h = letter_render.get_size()
        except:
            letter = None
            letter_w = 0
            letter_h = 0
        return (letter, letter_w, letter_h)

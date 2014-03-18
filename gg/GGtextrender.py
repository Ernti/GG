'''
Created on 17 Feb 2014

@author: tore
'''

import os
import pygame
import sys

from OpenGL.GL import *


class TextRender(object):

    def __init__(self, ggci):

        self.ggci = ggci

        pygame.font.init()

        if not pygame.font.get_init():
            print('Could not render font.')
            sys.exit(0)
        self.font = pygame.font.Font(os.path.join(".", "gg", "data", "fonts", "arial.ttf"), 18)
        self.char = []
        for c in range(256):
            self.char.append(self.createCharacter(chr(c), (255, 255, 255), (0, 0, 0)))
        self.char = tuple(self.char)
        self.lw = self.char[ord('0')][1]
        self.lh = self.char[ord('0')][2]
        self.angle = 0.0
        self.font = pygame.font.Font(os.path.join(".", "gg", "data", "fonts", "arial.ttf"), 50)
        self.char2 = []
        for c in range(256):
            self.char2.append(self.createCharacter(chr(c), (255, 255, 255), (0, 0, 0)))
        self.char2 = tuple(self.char2)
        self.lw2 = self.char2[ord('0')][1]
        self.lh2 = self.char2[ord('0')][2]
        self.angle2 = 0.0
        self.font = pygame.font.Font(os.path.join(".", "gg", "data", "fonts", "arial.ttf"), 12)
        self.statchar = []
        for c in range(256):
            self.statchar.append(self.createCharacter(chr(c), (0, 0, 0), (127, 127, 127)))
        self.statchar = tuple(self.statchar)
        self.statlw = self.statchar[ord('0')][1]
        self.statlh = self.statchar[ord('0')][2]
        self.statangle = 0.0

    def print(self, s, char, x, y, align):
        s = str(s)
        i = 0
        lx = 0
        length = len(s)

        if align == "center":
            while i < length:
                ch = char[ord(s[i])]
                lx += ch[1]
                i += 1

            lx = -lx / 2
            i = 0

            while i < length:
                glRasterPos2f(x + lx, y)
                ch = char[ord(s[i])]
                glDrawPixels(ch[1], ch[2], GL_RGBA, GL_UNSIGNED_BYTE, ch[0])
                lx += ch[1]
                i += 1

        elif align == "left":
            while i < length:
                glRasterPos2f(x + lx, y)
                ch = char[ord(s[i])]
                glDrawPixels(ch[1], ch[2], GL_RGBA, GL_UNSIGNED_BYTE, ch[0])
                lx += ch[1]
                i += 1

        elif align == "right":
            while i < length:
                glRasterPos2f(x - lx, y)
                ch = char[ord(s[i])]
                glDrawPixels(ch[1], ch[2], GL_RGBA, GL_UNSIGNED_BYTE, ch[0])
                lx -= ch[1]
                i += 1

    def textView(self):
        glViewport(0, 0, self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.ggci.ggdata.screenwidth - 1.0, 0.0, self.ggci.ggdata.screenheight - 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def createCharacter(self, s, fc, bg):
        try:
            letter_render = self.font.render(s, 1, fc, bg)
            letter = pygame.image.tostring(letter_render, 'RGBA', 1)
            letter_w, letter_h = letter_render.get_size()

        except:
            letter = None
            letter_w = 0
            letter_h = 0
        return letter, letter_w, letter_h
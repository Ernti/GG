'''
Created on 15 Apr 2014

@author: tore
'''

from OpenGL.GL import *


class WindowList(object):

    def __init__(self, window, list, x, y, w, h, rows):

        self.window = window
        self.list = list
        self.posx = x
        self.posy = y
        self.width = w
        self.height = h
        self.rows = rows
        self.toprow = 0

    def render(self):

        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        glVertex2f(self.window.posx + self.posx,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy)
        glVertex2f(self.window.posx + self.posx + self.width,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy)
        glVertex2f(self.window.posx + self.posx + self.width,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy - self.height)
        glVertex2f(self.window.posx + self.posx,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy - self.height)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(self.window.posx + self.posx,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy)
        glVertex2f(self.window.posx + self.posx + self.width,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy)
        glVertex2f(self.window.posx + self.posx + self.width,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy - self.height)
        glVertex2f(self.window.posx + self.posx,
                   self.window.ggci.ggdata.screenheight - self.window.posy - self.posy - self.height)
        glEnd()

        for i in range(self.toprow, self.rows):

            self.window.ggci.textrender.print(self.list[i].name, self.window.ggci.textrender.statchar,
                                              self.window.posx + self.posx + 2,
                                              self.window.posy - self.posy
                                              - (i * (2 + self.window.ggci.textrender.statchar[49][2])),
                                              "left")
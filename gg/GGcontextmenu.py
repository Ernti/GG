'''
Created on 27 Apr 2014

@author: tore
'''

from OpenGL.GL import *


class ContextMenu(object):

    def __init__(self, item, pos, ggci):

        self.ggci = ggci
        self.item = item
        self.posx = pos[0]
        self.posy = pos[1]
        self.buttons = []
        self.width = 100
        self.height = self.ggci.textrender.statchar[49][2] * len(self.buttons)

    def render(self):

        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        glVertex2f(self.posx,
                   self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width,
                   self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width,
                   self.ggci.ggdata.screenheight - self.posy - self.height)
        glVertex2f(self.posx,
                   self.ggci.ggdata.screenheight - self.posy - self.height)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(self.posx,
                   self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width,
                   self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width,
                   self.ggci.ggdata.screenheight - self.posy - self.height)
        glVertex2f(self.posx,
                   self.ggci.ggdata.screenheight - self.posy - self.height)
        glEnd()

        for button in self.buttons:

            button.render()

    def addButtons(self, buttons):

        self.buttons = buttons
        self.height = self.ggci.textrender.statchar[49][2] * len(self.buttons)
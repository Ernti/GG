'''
Created on 1 Mar 2014

@author: tore
'''

from OpenGL.GL import *
import pygame


class WindowButton(object):

    def __init__(self, window, text, x, y, w, h, action):

        self.window = window
        self.text = text
        self.posx = x
        self.posy = y
        self.width = w
        self.height = h
        self.actiondict = {'action': action}

    def render(self):

        mousepos = pygame.mouse.get_pos()

        glBegin(GL_QUADS)
        if ((mousepos[0] < self.window.posx + self.posx + self.width
             and mousepos[0] > self.window.posx + self.posx)
            and (mousepos[1] > self.window.posy + self.posy
                 and mousepos[1] < self.window.posy + self.posy + self.height)):
            glColor3f(0.7, 0.7, 0.7)
        else:
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

        self.window.ggci.textrender.print(self.text, self.window.ggci.textrender.statchar,
                                          self.window.posx + self.posx + self.width / 2,
                                          self.window.ggci.ggdata.screenheight - self.window.posy - self.posy
                                          - ((self.height + self.window.ggci.textrender.statchar[49][2]) / 2),
                                          "center")

    def action(self):

        self.window.ggci.buttonhandler.handle(self.actiondict)
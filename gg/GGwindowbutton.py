'''
Created on 1 Mar 2014

@author: tore
'''

from OpenGL.GL import *

class Windowbutton(object):

    def __init__(self, window, text, x, y, w, h, actiondict):

        self.window = window
        self.text = text
        self.posx = x
        self.posy = y
        self.width = w
        self.height = h
        self.actiondict = actiondict

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

        self.window.ggci.textrender.print(self.text, self.window.ggci.textrender.statchar,
                                          self.window.posx + self.posx + self.width / 2,
                                          self.window.ggci.ggdata.screenheight - self.window.posy - self.posy
                                          - ((self.height + self.window.ggci.textrender.statchar[49][2]) / 2),
                                          "center")

    def action(self):

        self.window.ggci.buttonhandler.handle(self.actiondict)
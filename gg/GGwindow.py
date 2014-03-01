'''
Created on 28 Feb 2014

@author: tore
'''

from OpenGL.GL import *

class Window(object):

    def __init__(self, title, posx, posy, width, height, ggci):

        self.ggci = ggci
        self.posx = posx
        self.posy = posy
        self.size = (self.width, self.height) = (width, height)
        self.title = title
        self.text = []

        self.visible = False

    def render(self):

        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy - self.height)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy - self.height)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy - self.height)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy - self.height)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glColor3f(0.4, 0.4, 0.4)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy)
        glVertex2f(self.posx + self.width, self.ggci.ggdata.screenheight - self.posy - 20)
        glVertex2f(self.posx, self.ggci.ggdata.screenheight - self.posy - 20)
        glEnd()

        self.ggci.textrender.print(self.title, self.ggci.textrender.statchar, self.posx + 5, self.ggci.ggdata.screenheight - self.posy - 17, "left")

        for text in self.text:

            self.ggci.textrender.print(text, self.ggci.textrender.statchar, self.posx + 5, self.ggci.ggdata.screenheight - self.posy - 38 - self.text.index(text)* 15, "left")

    def show(self):

        if self.visible is False:
            self.ggci.objectlist.addWindow(self)
            self.visible = True

    def hide(self):

        if self.visible is True:
            self.ggci.objectlist.removeWindow(self)
            self.visible = False

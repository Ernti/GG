'''
Created on 23 Feb 2014

@author: tore
'''

from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt


class Status(object):

    def __init__(self, ggci):

        self.ggci = ggci

    def render(self):

        glBegin(GL_QUADS)
        glColor(0.5, 0.5, 0.5)
        glVertex3f(-7.3, 4.1, 0)
        glVertex3f(-5, 4.1, 0)
        glVertex3f(-5, 2, 0)
        glVertex3f(-7.3, 2, 0)
        glEnd()

        glViewport(0, 0, self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.ggci.ggdata.screenwidth - 1.0, 0.0, self.ggci.ggdata.screenheight - 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.ggci.textrender.print("Insert Status Here", self.ggci.textrender.statchar, 12, 695, "left")

        if self.ggci.ggdata.screenheight == 0: self.ggci.ggdata.screenheight = 1
        glViewport(0, 0, self.ggci.ggdata.screenwidth, self.ggci.ggdata.screenheight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(self.ggci.ggdata.screenwidth) / float(self.ggci.ggdata.screenheight), 0.1, 1000.0)
        #glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
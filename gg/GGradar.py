'''
Created on 23 Feb 2014

@author: tore
'''

import math
from OpenGL.GL import *

class Radar(object):

    def __init__(self, ggci):

        self.ggci = ggci
        self.r = 100.0
        self.angle = 0

    def render(self):

        glLineWidth(3.0)

        self.r = 100.0
        self.angle = 0
        glBegin(GL_POLYGON)
        while self.angle < 2 * math.pi:
            glColor3f(0, 0, 0)
            glVertex2f(self.ggci.ggdata.screenwidth - 110 + self.r * math.cos(self.angle),
                       self.ggci.ggdata.screenheight - 110 + self.r * math.sin(self.angle))
            self.angle += 0.1
        glEnd()

        self.r = 100.0
        self.angle = 0
        glBegin(GL_LINE_LOOP)
        while self.angle < 2 * math.pi:
            glColor3f(0.5, 0.5, 0.5)
            glVertex2f(self.ggci.ggdata.screenwidth - 110 + self.r * math.cos(self.angle),
                       self.ggci.ggdata.screenheight - 110 + self.r * math.sin(self.angle))
            self.angle += 0.1
        glEnd()

        glLineWidth(1.5)

        i = 1
        while i < self.ggci.player.playership.radarrange / 25:

            self.r = 100 - (i * 100 / (self.ggci.player.playership.radarrange / 25))
            self.angle = 0
            glBegin(GL_LINE_LOOP)
            while self.angle < 2 * math.pi:
                glColor3f(0.1, 0.1, 0.1)
                glVertex2f(self.ggci.ggdata.screenwidth - 110 + self.r * math.cos(self.angle),
                           self.ggci.ggdata.screenheight - 110 + self.r * math.sin(self.angle))
                self.angle += 0.1
            glEnd()
            i += 1

        for objects in self.ggci.objectlist.objectlist:

            if objects.type is "ss":

                if objects.id is -1:
                    glBegin(GL_POINTS)
                    glColor(0, 1, 0)
                    glVertex2f(self.ggci.ggdata.screenwidth - 110, self.ggci.ggdata.screenheight - 110)
                    glEnd()
                elif math.sqrt(((objects.x - self.ggci.player.playership.x)
                                    / self.ggci.player.playership.radarrange)**2
                        + ((objects.y - self.ggci.player.playership.y)
                               / self.ggci.player.playership.radarrange) ** 2) < 1:

                    glBegin(GL_POINTS)
                    glColor(1, 0, 0)
                    glVertex2f(self.ggci.ggdata.screenwidth - 110 + ((objects.x - self.ggci.player.playership.x)
                                                                     / self.ggci.player.playership.radarrange)*100,
                               self.ggci.ggdata.screenheight - 110 + ((objects.y - self.ggci.player.playership.y)
                                                                      / self.ggci.player.playership.radarrange)*100)
                    glEnd()

        self.ggci.textrender.print("x: " + str(int(self.ggci.player.playership.x))
                                   + ", y: " + str(int(self.ggci.player.playership.y)),
                                   self.ggci.textrender.char,
                                   self.ggci.ggdata.screenwidth - 110,
                                   self.ggci.ggdata.screenheight - 215 - self.ggci.textrender.char[49][2],
                                   'center')
'''
Created on 23 Feb 2014

@author: tore
'''

import math
from OpenGL.GL import *

class Radar(object):

    def __init__(self, ggci):

        self.ggci = ggci
        self.r = 1.0
        self.angle = 0

    def render(self):

        self.r = 1.0
        self.angle = 0
        glBegin(GL_POLYGON)
        while self.angle < 2 * math.pi:
            glColor3f(0, 0, 0)
            glVertex3f(6 + self.r * math.cos(self.angle), 3 + self.r * math.sin(self.angle), 0)
            self.angle += 0.1
        glEnd()

        self.r = 1.0
        self.angle = 0
        glBegin(GL_LINE_LOOP)
        while self.angle < 2 * math.pi:
            glColor3f(0.5, 0.5, 0.5)
            glVertex3f(6 + self.r * math.cos(self.angle), 3 + self.r * math.sin(self.angle), 0)
            self.angle += 0.1
        glEnd()

        i = 1
        while i < self.ggci.player.playership.radarrange / 25:

            self.r = 1 - (i / (self.ggci.player.playership.radarrange / 25))
            self.angle = 0
            glBegin(GL_LINE_LOOP)
            while self.angle < 2 * math.pi:
                glColor3f(0.1, 0.1, 0.1)
                glVertex3f(6 + self.r * math.cos(self.angle), 3 + self.r * math.sin(self.angle), 0)
                self.angle += 0.1
            glEnd()
            i += 1

        for objects in self.ggci.objectlist.objectlist:

            if objects.id is -1:
                glBegin(GL_POINTS)
                glColor(0, 1, 0)
                glVertex3f(6 + (objects.x - self.ggci.player.playership.x) / self.ggci.player.playership.radarrange,
                           3 + (objects.y - self.ggci.player.playership.y) / self.ggci.player.playership.radarrange, 0)
                glEnd()
            elif  math.sqrt(((objects.x - self.ggci.player.playership.x) / self.ggci.player.playership.radarrange)**2
                    + ((objects.y - self.ggci.player.playership.y) / self.ggci.player.playership.radarrange) ** 2) < 1:
                glBegin(GL_POINTS)
                glColor(1, 0, 0)
                glVertex3f(6 + (objects.x - self.ggci.player.playership.x) / self.ggci.player.playership.radarrange,
                           3 + (objects.y - self.ggci.player.playership.y) / self.ggci.player.playership.radarrange, 0)
                glEnd()
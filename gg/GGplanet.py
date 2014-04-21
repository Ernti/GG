'''
Created on 21 Apr 2014

@author: tore
'''

import math
from OpenGL.GL import *


class Planet(object):

    def __init__(self, id, x, y, ggci):

        self.ggci = ggci
        self.id = id
        self.type = "Planet"
        self.x = x
        self.y = y

        self.r = 100.0
        self.angle = 0

    def action(self):

        self.r = 100.0
        self.angle = 0

    def render(self):

        self.r = 100.0
        self.angle = 0
        glBegin(GL_POLYGON)
        while self.angle < 2 * math.pi:
            glColor3f(0, 0.5, 0.5)
            glVertex3f(self.ggci.player.x + self.x + self.r * math.cos(self.angle),
                       self.ggci.player.y + self.y + self.r * math.sin(self.angle),
                       0-100 - self.ggci.player.z)
            self.angle += 0.1
        glEnd()
'''
Created on 20 Feb 2014

@author: tore
'''


from OpenGL.GL import glBegin, GL_TRIANGLES, glColor, glVertex3f, glEnd
import math


class Engine(object):

    def __init__(self, data, ss):

        self.ss = ss
        self.type = data['type']
        self.thrust = data['thrust']
        self.mass = data['mass']

    def render(self):

        [glBegin(GL_TRIANGLES),
        glColor(0.3, 0.3, 0.3), glVertex3f(self.ss.x + self.ss.ggci.player.x,
                                       self.ss.y + self.ss.ggci.player.y,
                                       0 - self.ss.ggci.player.z),

        glColor(0.3, 0.3, 0.3), glVertex3f(self.ss.x + self.ss.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.ss.angle + 160))),
                                       self.ss.y + self.ss.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.ss.angle + 160))),
                                       0 - self.ss.ggci.player.z),

        glColor(0.3, 0.3, 0.3), glVertex3f(self.ss.x + self.ss.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.ss.angle + 200))),
                                       self.ss.y + self.ss.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.ss.angle + 200))),
                                       0 - self.ss.ggci.player.z),
        glEnd()]
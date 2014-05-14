'''
Created on 21 Apr 2014

@author: tore
'''

import math
from OpenGL.GL import *
import pygame


class Planet(object):

    def __init__(self, id, orbitx, orbity, orbitr, orbitspeed, ggci):

        self.ggci = ggci
        self.id = id
        self.type = "planet"

        self.orbitx = orbitx
        self.orbity = orbity
        self.orbitr = orbitr
        self.orbitangle = 0
        self.orbitspeed = orbitspeed
        self.x = math.cos(self.orbitangle) * self.orbitr + self.orbitx
        self.y = math.sin(self.orbitangle) * self.orbitr + self.orbity

        self.r = 100.0
        self.angle = 0

        self.vertex = [[self.r, self.r, 0], [-self.r, -self.r, 0]]

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick

    def action(self):

        self.nowtick = pygame.time.get_ticks()

        self.orbitangle += self.orbitspeed * ((self.nowtick - self.lasttick) / 1000)
        if self.orbitangle > 360:
            self.orbitangle -= 360

        self.x = math.cos(self.orbitangle) * self.orbitr + self.orbitx
        self.y = math.sin(self.orbitangle) * self.orbitr + self.orbity

        self.lasttick = self.nowtick

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

    def debugRender(self):

        glColor(0, 0.8, 0.2)

        glBegin(GL_LINE_LOOP)
        glVertex3f(self.collisionbox[0] + self.x + self.ggci.player.x,
                   self.collisionbox[2] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[1] + self.x + self.ggci.player.x,
                   self.collisionbox[2] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[1] + self.x + self.ggci.player.x,
                   self.collisionbox[3] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[0] + self.x + self.ggci.player.x,
                   self.collisionbox[3] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glEnd()
'''
Created on 8 Dec 2013

@author: tore
'''


import math

from OpenGL.GL import glBegin, GL_TRIANGLES, glColor, glVertex3f, glEnd
import pygame


# from OpenGL.GLU import *
class SpaceShip(object):

    def __init__(self, ssid, x, y, ggci):

        self.ggci = ggci
        self.id = ssid
        self.oxygen = 100
        self.hull = 0
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.angle = 0
        self.speed = 0
        self.mass = 10000
        self.turntime = 10
        self.acceleration = 0
        self.thrust = 100

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick

    def render(self):

        self.nowtick = pygame.time.get_ticks()

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.x = self.x + (self.velocity_x * ((self.nowtick
                                               - self.lasttick) / 100))
        self.y = self.y + (self.velocity_y * ((self.nowtick
                                               - self.lasttick) / 100))

        self.lasttick = self.nowtick

        [glBegin(GL_TRIANGLES),
        glColor(255, 0, 0), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle)) * 1),
                                       0 - self.ggci.player.z),

        glColor(0, 255, 0), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 120)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 120)) * 1),
                                       0 - self.ggci.player.z),

        glColor(0, 0, 255), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 240)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 240)) * 1),
                                       0 - self.ggci.player.z),
        glEnd()]

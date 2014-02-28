'''
Created on 25 Feb 2014

@author: tore
'''

import pygame
import math
from OpenGL.GL import *


class Bullet(object):

    def __init__(self, data, ggci):

        self.ggci = ggci
        self.id = data['soid']
        self.type = "bullet"
        self.pos = (self.x, self.y) = (data['x'], data['y'])
        self.angle = data['r']
        self.speed = 10

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.render_nowtick = pygame.time.get_ticks()
        self.render_lasttick = self.render_nowtick

    def move(self):

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.pos = (self.pos[0] + (self.velocity_x * ((self.render_nowtick - self.render_lasttick) / 1000)),
                    self.pos[1] + (self.velocity_y * ((self.render_nowtick - self.render_lasttick) / 1000)))

        glBegin(GL_POINTS)
        glColor(0.4, 0.4, 0.4)
        glVertex3f(self.pos[0], self.pos[1], 0 - self.ggci.player.z)
        glEnd()

        self.render_lasttick = self.render_nowtick
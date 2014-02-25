'''
Created on 25 Feb 2014

@author: tore
'''
import pygame
import math
from OpenGL.GL import *


class Bullet(object):

    def __init__(self, startpos, angle, ggci):

        self.ggci = ggci
        self.id = 1000
        self.type = "bullet"
        self.pos = startpos
        self.angle = angle
        self.speed = 100

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.render_nowtick = pygame.time.get_ticks()
        self.render_lasttick = self.render_nowtick

        pygame.event.post(pygame.event.Event(
                                    26, {'type': 'playershot',
                                    'soid': self.id,
                                    'x': self.pos[0],
                                    'y': self.pos[1],
                                    'speed': self.speed,
                                    'r': self.angle,
                                    'scale_x': self.scale_x,
                                    'scale_y': self.scale_y}))

    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.pos[0] = self.pos[0] + (self.velocity_x * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))
        self.pos[1] = self.pos[1] + (self.velocity_y * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))

        glBegin(GL_POINTS)
        glColor(0.4, 0.4, 0.4)
        glVertex3f(self.pos[0], self.pos[1], 0 - self.ggci.player.z)
        glEnd()

        self.render_lasttick = self.render_nowtick
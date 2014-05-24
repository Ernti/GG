'''
Created on 25 Feb 2014

@author: tore
'''

import pygame
import math
from OpenGL.GL import *


class Bullet(object):

    def __init__(self, data, ggci):

        """

        @type data: dictionary('soid': ,'x': ,'y': ,'r':)
        """
        self.ggci = ggci
        self.id = -2
        self.type = "bullet"
        self.x = data['x']
        self.y = data['y']
        self.r = data['r']
        self.speed = 10

        self.scale_x = math.cos(math.radians(self.r))
        self.scale_y = math.sin(math.radians(self.r))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.render_nowtick = pygame.time.get_ticks()
        self.render_lasttick = self.render_nowtick

        print('PEW!')

    def action(self):

        for object in self.ggci.objectlist.objectlist:

            if object.id is not -1 and object is not self:

                x = abs(object.x - self.x)
                y = abs(object.y - self.y)
                a = math.sqrt(x**2+y**2)

                if a < 2:
                    self.ggci.objectlist.removeObject(self)
                    print(str(object.id) + ' hit!')

        self.scale_x = math.cos(math.radians(self.r))
        self.scale_y = math.sin(math.radians(self.r))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.x += self.velocity_x * ((self.render_nowtick - self.render_lasttick) / 1000)
        self.y += self.velocity_y * ((self.render_nowtick - self.render_lasttick) / 1000)

        #self.x = self.x + (self.velocity_x * ((self.render_nowtick - self.render_lasttick) / 1000))
        #self.y = self.y + (self.velocity_y * ((self.render_nowtick - self.render_lasttick) / 1000))

        glBegin(GL_POINTS)
        glColor(0, 1, 0)
        glVertex3f(self.x, self.y, 0 - self.ggci.player.z)
        glEnd()

        self.render_lasttick = self.render_nowtick
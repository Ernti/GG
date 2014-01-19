'''
Created on 8 Dec 2013

@author: tore
'''
import math
import os.path

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame.image


class SpaceShip(object):

    def __init__(self, ssid, x, y, ggci):

        self.ggci = ggci
        self.id = ssid
        self.oxygen = 100
        self.hull = 0
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0.01

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.now = pygame.time.get_ticks()
        self.after = pygame.time.get_ticks()

    def render(self):

        # self.img = pygame.transform.rotozoom(self.img, 0, 1)
        # objects.ssrect = objects.ssimg.get_rect()
        # self.rect.x = self.x + player.x
        # self.rect.y = self.y + player.y

        # self.img.set_colorkey((255, 0, 255))
        # background.blit(self.img, self.rect)

        [glBegin(GL_TRIANGLES),
        glColor(255, 0, 0), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle)) * 1), 0 - self.ggci.player.z),
        glColor(0, 255, 0), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 120)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 120)) * 1), 0 - self.ggci.player.z),
        glColor(0, 0, 255), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 240)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 240)) * 1), 0 - self.ggci.player.z),
        glEnd()]

'''
Created on 8 Dec 2013

@author: tore
'''


import math
import numpy

from OpenGL.GL import GL_POLYGON, glVertexPointerf, glDrawElementsui, GL_VERTEX_ARRAY, glEnableClientState, glColor
import pygame
from gg.GGspaceshipengine import Engine
from gg.GGspaceshipweapon import Weapon


class SpaceShip(object):

    def __init__(self, data, ggci):

        self.ggci = ggci
        self.id = data['soid']
        self.type = "ss"

        self.oxygen = 100
        self.hull = 100

        self.x = data['x']
        self.nextx = self.x
        self.y = data['y']
        self.nexty = self.y
        self.lastx = self.x
        self.lasty = self.y

        self.r = 0
        self.nextr = self.r
        self.velocity_r = 0

        self.speed = 0
        self.turntime = 1
        self.acceleration = 0

        self.engine = Engine(data['engine'], self)
        self.weapon = Weapon("Machine Gun", self.ggci)
        self.inventory = []

        self.radarrange = 250

        self.mass = self.engine.mass
        self.thrust = self.engine.thrust

        self.scale_x = math.cos(math.radians(self.r))
        self.scale_y = math.sin(math.radians(self.r))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.turntime = (self.thrust / (self.mass ** 1.08) * 1000)

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.render_nowtick = pygame.time.get_ticks()
        self.render_lasttick = self.render_nowtick

        self.vertex = numpy.array([numpy.array([3, 0, 0], 'f').reshape(1, 3),
                                   numpy.array([-1, -2, 0], 'f').reshape(1, 3),
                                   numpy.array([-0.5, 0, 0], 'f').reshape(1, 3),
                                   numpy.array([-1, 2, 0], 'f').reshape(1, 3)])

        self.indices = numpy.arange(0, len(self.vertex), None, 'i')
        print(len(self.vertex))

    def move(self, nextx, nexty, nextr):

        self.nextx = nextx
        self.nexty = nexty
        self.nextr = nextr

        self.nowtick = pygame.time.get_ticks()

    def action(self):

        self.velocity_x = (self.nextx - self.x)
        self.velocity_y = (self.nexty - self.y)
        self.velocity_r = (self.nextr - self.r)

        if self.velocity_r > 180:
            self.velocity_r -= 360

        if self.velocity_r < -180:
            self.velocity_r += 360

        self.lasttick = self.nowtick

    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.x = self.x + (self.velocity_x * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))
        self.y = self.y + (self.velocity_y * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))
        self.r = self.r + (self.velocity_r * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))

        if self.r > 180:
            self.r -= 360

        if self.r < -180:
            self.r += 360

        glColor(0.2, 0.2, 0.2)

        self.engine.render()

        vertex = []

        for vert, verts in enumerate(self.vertex):

            vx = numpy.dot(self.vertex[vert], numpy.array([math.cos(math.radians(self.r)),
                                                                    math.sin(math.radians(self.r)), 0,
                                                                    -math.sin(math.radians(self.r)),
                                                                    math.cos(math.radians(self.r)), 0,
                                                                    0, 0, 1], 'f').reshape(3, 3))

            vx = vx + numpy.array([self.x + self.ggci.player.x, self.y + self.ggci.player.y, 0 - self.ggci.player.z],
                                  'f').reshape(1, 3)

            vertex.append(vx)

        vertex = numpy.array(vertex, 'f').reshape(len(self.vertex), 3)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(vertex)
        glDrawElementsui(GL_POLYGON, self.indices)

        self.render_lasttick = self.render_nowtick

    def renderNameplate(self):


        textx = (((self.x + self.ggci.player.x)
                  / ((math.tan(math.radians(45 / 2)) * (self.ggci.ggdata.screenwidth / self.ggci.ggdata.screenheight))
                     * (10 + self.ggci.player.z))
                  * self.ggci.ggdata.screenwidth / 2) + self.ggci.ggdata.screenwidth / 2)

        texty = (((self.y + self.ggci.player.y + 1)
                  / (math.tan(math.radians(45 / 2)) * (10 + self.ggci.player.z))
                  * self.ggci.ggdata.screenheight / 2) + self.ggci.ggdata.screenheight / 2)

        self.ggci.textrender.print(self.id, self.ggci.textrender.char, textx, texty, "center")



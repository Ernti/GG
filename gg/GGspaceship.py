'''
Created on 8 Dec 2013

@author: tore
'''


import math
import numpy

from OpenGL.GL import *
import pygame
from gg.GGspaceshipengine import Engine
from gg.GGspaceshipweapon import Weapon


class SpaceShip(object):

    def __init__(self, data, ggci):

        self.ggci = ggci
        self.id = data['soid']
        self.type = "ss"

        self.debug = False

        self.oxygen = 100
        self.hull = 100

        self.target = (0, 0)
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
        self.weapon = Weapon(self, "Machine Gun", self.ggci)
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
                                   numpy.array([0, 0.5, 0], 'f').reshape(1, 3),
                                   numpy.array([-1, 2, 0], 'f').reshape(1, 3),
                                   numpy.array([-0.5, 0, 0], 'f').reshape(1, 3),
                                   numpy.array([-1, -2, 0], 'f').reshape(1, 3),
                                   numpy.array([0, -0.5, 0], 'f').reshape(1, 3)])

        self.indices = numpy.arange(0, len(self.vertex), None, 'i')
        print(len(self.vertex))

        self.collisionbox = [0, 0, 0, 0]
        self.collisionvertex = self.vertex.reshape(len(self.vertex), 3)
        for vert in self.collisionvertex:
            if vert[0] < self.collisionbox[0]:
                self.collisionbox[0] = vert[0]
            if vert[0] > self.collisionbox[1]:
                self.collisionbox[1] = vert[0]
            if vert[1] < self.collisionbox[2]:
                self.collisionbox[2] = vert[1]
            if vert[1] > self.collisionbox[3]:
                self.collisionbox[3] = vert[1]
        print(self.collisionbox)

    def move(self, target):

        self.target = target

    def action(self):

        self.nowtick = pygame.time.get_ticks()

        if (self.x, self.y) != self.target:

            self.targetangle = math.degrees(math.atan2((self.target[1] - self.y),
                                                       (self.target[0] - self.x)))

            if self.targetangle - self.r > 180:

                self.turnRight()

            elif self.targetangle - self.r < (-180):

                self.turnLeft()

            elif (self.targetangle - self.r > 0
                  and self.targetangle - self.r < 180):

                self.turnLeft()

            elif (self.targetangle - self.r < 0
                  and self.targetangle - self.r > (-180)):

                self.turnRight()

            self.speedUp()

        else:

            self.target = (self.x, self.y)

        self.lasttick = self.nowtick

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)


# else:
#
# if self.after < (self.nowtick - 1000):
#
# pygame.event.post(pygame.event.Event(
# 26, {'type': 'playermoved',
# 'x': self.playership.x,
# 'y': self.playership.y,
# 'r': self.playership.angle}))
#
# self.after = pygame.time.get_ticks()


    def speedUp(self):

        self.acceleration = (self.thrust / (self.mass ** 1.08) * 100)

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        stopx = (self.velocity_x * (self.mass ** 1.08) / self.thrust / 6)
        stopy = (self.velocity_y * (self.mass ** 1.08) / self.thrust / 6)

        if (abs(self.target[0] - self.x) >= 0.1 + abs(stopx) or abs(self.target[1] - self.y) >= 0.1 + abs(stopy)):

            if self.speed < ((self.acceleration * (self.mass ** 1.08) / self.thrust / 6)):

                self.speed += (self.acceleration * ((self.nowtick - self.lasttick) / 1000))

            else:

                self.speed = ((self.acceleration * (self.mass ** 1.08) / self.thrust / 6))

        else:

            self.slowDown()

    def slowDown(self):

        self.acceleration = (self.thrust / (self.mass ** 1.08) * 100)

        if (self.speed - (self.acceleration * ((self.nowtick - self.lasttick) / 1000))) > 0.01:

            self.speed -= (self.acceleration * ((self.nowtick - self.lasttick) / 1000))

        else:

            self.speed = 0

    def turnLeft(self):

        self.turntime = (self.thrust / (self.mass ** 1.08) * 1000)

        if abs(self.targetangle - self.r) > (self.turntime * ((self.nowtick - self.lasttick) / 1000)):

            self.slowDown()
            self.r += (self.turntime * ((self.nowtick - self.lasttick) / 1000))

            if self.r > 180:

                self.r -= 360

        else:

            self.r = self.targetangle

        self.scale_x = math.cos(math.radians(self.r))
        self.scale_y = math.sin(math.radians(self.r))

    def turnRight(self):

        self.turntime = (self.thrust / (self.mass ** 1.08) * 1000)

        if (abs(self.targetangle - self.r) > (self.turntime * ((self.nowtick - self.lasttick) / 1000))):

            self.slowDown()

            self.r -= (self.turntime * ((self.nowtick - self.lasttick) / 1000))

            if self.r < -180:

                self.r += 360

        else:

            self.r = self.targetangle

        self.scale_x = math.cos(math.radians(self.r))
        self.scale_y = math.sin(math.radians(self.r))



    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.x += self.velocity_x * ((self.render_nowtick - self.render_lasttick) / 1000)
        self.y += self.velocity_y * ((self.render_nowtick - self.render_lasttick) / 1000)
        self.r += self.velocity_r * ((self.render_nowtick - self.render_lasttick) / 1000)

        #print(self.velocity_x * ((self.render_nowtick - self.render_lasttick) / 1000), self.velocity_y * ((self.render_nowtick - self.render_lasttick) / 1000))

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

        if self.debug is True:
            self.debugRender()

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



'''
Created on 8 Dec 2013

@author: tore
'''


import math

from OpenGL.GL import glBegin, GL_TRIANGLES, glColor, glVertex3f, glEnd
import pygame
from gg.GGspaceshipengine import Engine
from gg.GGspaceshipweapon import Weapon


class SpaceShip(object):

    def __init__(self, data, ggci):

        self.ggci = ggci
        self.id = data['soid']
        self.type = "ss"

        self.oxygen = 100
        self.hull = 0

        self.x = data['x']
        self.y = data['y']
        self.target = (self.x, self.y)
        self.lastx = self.x
        self.lasty = self.y
        self.angle = 0
        self.targetangle = 0
        self.speed = 0
        self.turntime = 1
        self.acceleration = 0

        self.engine = Engine(data['engine'], self)
        self.weapon = Weapon("Machine Gun", self.ggci)

        self.radarrange = 250

        self.mass = self.engine.mass
        self.thrust = self.engine.thrust

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.render_nowtick = pygame.time.get_ticks()
        self.render_lasttick = self.render_nowtick

    def move(self):

        self.nowtick = pygame.time.get_ticks()

        if (self.x, self.y) != self.target:

            self.targetangle = math.degrees(math.atan2((self.target[1] - self.y),
                                                       (self.target[0] - self.x)))

            if self.targetangle - self.angle > 180:

                self.turnRight()

            elif self.targetangle - self.angle < (-180):

                self.turnLeft()

            elif (self.targetangle - self.angle > 0
                  and self.targetangle - self.angle < 180):

                self.turnLeft()

            elif (self.targetangle - self.angle < 0
                  and self.targetangle - self.angle > (-180)):

                self.turnRight()

            self.speedUp()

        self.lasttick = self.nowtick

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

        if abs(self.targetangle - self.angle) > (self.turntime * ((self.nowtick - self.lasttick) / 1000)):

            self.slowDown()
            self.angle += (self.turntime * ((self.nowtick - self.lasttick) / 1000))

            if self.angle > 180:

                self.angle -= 360

        else:

            self.angle = self.targetangle

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

    def turnRight(self):

        self.turntime = (self.thrust / (self.mass ** 1.08) * 1000)

        if (abs(self.targetangle - self.angle) > (self.turntime * ((self.nowtick - self.lasttick) / 1000))):

            self.slowDown()

            self.angle -= (self.turntime * ((self.nowtick - self.lasttick) / 1000))

            if self.angle < -180:

                self.angle += 360

        else:

            self.angle = self.targetangle

        self.scale_x = math.cos(math.radians(self.angle))
        self.scale_y = math.sin(math.radians(self.angle))

    def render(self):

        self.render_nowtick = pygame.time.get_ticks()

        self.velocity_x = (self.speed * self.scale_x)
        self.velocity_y = (self.speed * self.scale_y)

        self.x = self.x + (self.velocity_x * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))
        self.y = self.y + (self.velocity_y * ((self.render_nowtick
                                               - self.render_lasttick) / 1000))

        self.engine.render()

        [glBegin(GL_TRIANGLES),
        glColor(0.4, 0.4, 0.4), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle)) * 1),
                                       0 - self.ggci.player.z),

        glColor(0.4, 0.4, 0.4), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 120)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 120)) * 1),
                                       0 - self.ggci.player.z),

        glColor(0.4, 0.4, 0.4), glVertex3f(self.x + self.ggci.player.x
                                       + (math.cos(math.radians(
                                          self.angle + 240)) * 1),
                                       self.y + self.ggci.player.y
                                       + (math.sin(math.radians(
                                          self.angle + 240)) * 1),
                                       0 - self.ggci.player.z),
        glEnd()]

        self.render_lasttick = self.render_nowtick

    def renderNameplate(self):


        textx = (((self.x + self.ggci.player.x)
                  / ((math.tan(math.radians(45 / 2)) * (self.ggci.ggdata.screenwidth / self.ggci.ggdata.screenheight)) * (10 + self.ggci.player.z))
                  * self.ggci.ggdata.screenwidth / 2) + self.ggci.ggdata.screenwidth / 2)

        texty = (((self.y + self.ggci.player.y + 1)
                  / (math.tan(math.radians(45 / 2)) * (10 + self.ggci.player.z))
                  * self.ggci.ggdata.screenheight / 2) + self.ggci.ggdata.screenheight / 2)

        self.ggci.textrender.print(self.id, self.ggci.textrender.char, textx, texty, "center")



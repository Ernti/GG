'''
Created on 16 Dec 2013

@author: tore
'''
import math

import pygame


class Player(object):

    def __init__(self, ggci):

        self.ggci = ggci
        self.playership = None
        self.x = 0
        self.y = 0
        self.z = 10

        self.target = (0, 0)
        self.targetangle = 0

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.after = pygame.time.get_ticks()

    def eventtest(self, uevent):

        self.uevent = uevent
        self.playership.scale_x = math.cos(math.radians(self.playership.angle))
        self.playership.scale_y = math.sin(math.radians(self.playership.angle))

        self.playership.velocity_x = (self.playership.speed
                                      * self.playership.scale_x)
        self.playership.velocity_y = (self.playership.speed
                                      * self.playership.scale_y)

        maxspeed = (((self.playership.thrust / (self.playership.mass ** 1.08)
                      * 100) * (self.playership.mass ** 1.08)
                     / self.playership.thrust / 6)) * 3.6

        print(maxspeed)

    def move(self):

        self.nowtick = pygame.time.get_ticks()

        if self.uevent.lock == True:

            self.x = -self.playership.x
            self.y = -self.playership.y

        if self.uevent.rmsbtn == True:

            self.uevent.target = pygame.mouse.get_pos()

            self.ggci.player.target = (-self.x + (((self.uevent.target[0]
                                    - self.ggci.ggdata.screenwidth / 2)
                                    / self.ggci.ggdata.screenwidth * 2)
                                    * ((math.tan(math.radians(45 / 2))
                                    * (self.ggci.ggdata.screenwidth
                                       / self.ggci.ggdata.screenheight))
                                       * (10 + self.z))),

                                    (-self.y + (-(self.uevent.target[1]
                                    - self.ggci.ggdata.screenheight / 2)
                                    / self.ggci.ggdata.screenheight * 2)
                                    * (math.tan(math.radians(45 / 2))
                                       * (10 + self.z))))

        if (self.playership.x, self.playership.y) != self.target:

            self.targetangle = math.degrees(math.atan2((self.target[1]
                                                        - self.playership.y),
                                                       (self.target[0]
                                                        - self.playership.x)))

            if self.targetangle - self.playership.angle > 180:

                self.turnRight()

            elif self.targetangle - self.playership.angle < (-180):

                self.turnLeft()

            elif (self.targetangle - self.playership.angle > 0
                  and self.targetangle - self.playership.angle < 180):

                self.turnLeft()

            elif (self.targetangle - self.playership.angle < 0
                  and self.targetangle - self.playership.angle > (-180)):

                self.turnRight()

            self.speedUp()

        self.lasttick = self.nowtick

        if self.playership.speed > 0:
            if self.after < (self.nowtick - 100):

                pygame.event.post(pygame.event.Event(
                                    26, {'type': 'playermoved',
                                    'soid': self.playership.id,
                                    'x': self.playership.x,
                                    'y': self.playership.y,
                                    'speed': self.playership.speed,
                                    'r': self.playership.angle,
                                    'scale_x': self.playership.scale_x,
                                    'scale_y': self.playership.scale_y}))

                self.after = pygame.time.get_ticks()

        else:

            if self.after < (self.nowtick - 1000):

                pygame.event.post(pygame.event.Event(
                                    26, {'type': 'playermoved',
                                    'soid': self.playership.id,
                                    'x': self.playership.x,
                                    'y': self.playership.y,
                                    'speed': self.playership.speed,
                                    'r': self.playership.angle,
                                    'scale_x': self.playership.scale_x,
                                    'scale_y': self.playership.scale_y}))

                self.after = pygame.time.get_ticks()

    def speedUp(self):

        self.playership.acceleration = (self.playership.thrust
                                        / (self.playership.mass ** 1.08) * 100)

        self.velocity_x = (self.playership.speed * self.playership.scale_x)
        self.velocity_y = (self.playership.speed * self.playership.scale_y)

        stopx = (self.velocity_x * (self.playership.mass ** 1.08)
                / self.playership.thrust / 6)
        stopy = (self.velocity_y * (self.playership.mass ** 1.08)
                / self.playership.thrust / 6)

        if (abs(self.target[0] - self.playership.x) >= 0.1 + abs(stopx)
            or abs(self.target[1] - self.playership.y) >= 0.1 + abs(stopy)):

            if self.playership.speed < ((self.playership.acceleration
                                         * (self.playership.mass ** 1.08)
                                         / self.playership.thrust / 6)):

                self.playership.speed += (self.playership.acceleration
                                          * ((self.nowtick - self.lasttick)
                                             / 1000))

            else:

                self.playership.speed = ((self.playership.acceleration
                                          * (self.playership.mass ** 1.08)
                                          / self.playership.thrust / 6))

        else:

            self.slowDown()

    def slowDown(self):

        self.playership.acceleration = (self.playership.thrust
                                        / (self.playership.mass ** 1.08)
                                        * 100)

        if (self.playership.speed - (self.playership.acceleration
                                        * ((self.nowtick - self.lasttick)
                                           / 1000))) > 0.01:

            self.playership.speed -= (self.playership.acceleration
                                        * ((self.nowtick - self.lasttick)
                                           / 1000))

        else:

            self.playership.speed = 0

    def turnLeft(self):

        self.playership.turntime = (self.playership.thrust
                                    / (self.playership.mass ** 1.08) * 1000)

        if  (abs(self.targetangle - self.playership.angle)
             > (self.playership.turntime * ((self.nowtick - self.lasttick)
                                            / 1000))):

            self.slowDown()
            self.playership.angle += (self.playership.turntime
                                      * ((self.nowtick - self.lasttick)
                                         / 1000))

            if self.playership.angle > 180:

                self.playership.angle -= 360

        else:

            self.playership.angle = self.targetangle

        self.playership.scale_x = math.cos(math.radians(self.playership.angle))
        self.playership.scale_y = math.sin(math.radians(self.playership.angle))

    def turnRight(self):

        self.playership.turntime = (self.playership.thrust
                                        / (self.playership.mass ** 1.08)
                                        * 1000)

        if  (abs(self.targetangle - self.playership.angle)
             > (self.playership.turntime * ((self.nowtick - self.lasttick)
                                            / 1000))):

            self.slowDown()

            self.playership.angle -= (self.playership.turntime
                                      * ((self.nowtick - self.lasttick)
                                         / 1000))

            if self.playership.angle < -180:

                self.playership.angle += 360

        else:

            self.playership.angle = self.targetangle

        self.playership.scale_x = math.cos(math.radians(self.playership.angle))
        self.playership.scale_y = math.sin(math.radians(self.playership.angle))

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

        self.target = (None, None)

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

    def move(self):

        # if self.playership.target != (self.playership.x, self.playership.y):

        # print(self.x, self.y)

        if self.uevent is not None:

            self.nowtick = pygame.time.get_ticks()

            if self.uevent.w == True:

                self.playership.acceleration = ((self.playership.thrust / (self.playership.mass ** 1.08)) * 0.85 ** (self.playership.speed * 100))

                if self.playership.acceleration < 0.001:

                    self.playership.acceleration = 0

                self.playership.speed = (self.playership.acceleration
                                         * ((self.nowtick - self.lasttick) / 100)) + self.playership.speed

                print(self.playership.speed * 100)

                # self.playership.velocity_x = (() * self.playership.scale_x)

                # self.playership.velocity_x = (self.playership.speed
                #                      * self.playership.scale_x)
                # self.playership.velocity_y = (self.playership.speed
                #                      * self.playership.scale_y)

                # self.y -= 10

                # self.rect = self.rect.move(0, -1)
            if self.uevent.s == True:

                if self.playership.speed > 0:

                    self.playership.acceleration = ((self.playership.thrust / (self.playership.mass ** 1.08)) * 0.85 ** (self.playership.speed * 100))

                    self.playership.speed = (self.playership.speed
                                             - (self.playership.acceleration
                                             * ((self.nowtick - self.lasttick)
                                                / 100)))

                else:

                    self.playership.speed = 0

                print(self.playership.speed * 100)

            if self.uevent.a == True:

                # self.x -= 10

                self.playership.angle += (self.playership.turntime
                                          * ((self.nowtick - self.lasttick)
                                             / 100))

                self.playership.scale_x = math.cos(math.radians(
                                                    self.playership.angle))
                self.playership.scale_y = math.sin(math.radians(
                                                    self.playership.angle))

            if self.uevent.d == True:

                # self.x += 10

                self.playership.angle -= (self.playership.turntime
                                          * ((self.nowtick - self.lasttick)
                                             / 100))

                self.playership.scale_x = math.cos(math.radians(
                                                    self.playership.angle))
                self.playership.scale_y = math.sin(math.radians(
                                                    self.playership.angle))

                # self.rect = self.rect.move(1, 0)
#            pygame.event.post(pygame.event.Event(26, {'type': 'playermoved',
#                                                 'soid': self.id,
#                                                 'x': self.x,
#                                                 'y': self.y}))

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

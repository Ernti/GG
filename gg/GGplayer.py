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

        self.nowtick = pygame.time.get_ticks()
        self.lasttick = self.nowtick
        self.after = pygame.time.get_ticks()

    def eventtest(self, uevent):

        self.uevent = uevent
        #self.playership.scale_x = math.cos(math.radians(self.playership.angle))
        #self.playership.scale_y = math.sin(math.radians(self.playership.angle))

        #self.playership.velocity_x = (self.playership.speed
        #                              * self.playership.scale_x)
        #self.playership.velocity_y = (self.playership.speed
        #                              * self.playership.scale_y)

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

            self.playership.target = (-self.x + (((self.uevent.target[0]
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

        self.playership.action()

        if self.playership.speed > 0:
            if self.after < (self.nowtick - 10):

                pygame.event.post(pygame.event.Event(
                                    26, {'type': 'playermoved',
                                    'soid': self.playership.id,
                                    'x': self.playership.x,
                                    'y': self.playership.y,
                                    'speed': self.playership.speed,
                                    'r': self.playership.angle,
                                    'scale_x': self.playership.scale_x,
                                    'scale_y': self.playership.scale_y,
                                    'target': self.playership.target,
                                    'engine': {'type': self.playership.engine.type,
                                               'thrust': self.playership.engine.thrust,
                                               'mass': self.playership.engine.mass}}))

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
                                    'scale_y': self.playership.scale_y,
                                    'target': self.playership.target,
                                    'engine': {'type': self.playership.engine.type,
                                               'thrust': self.playership.engine.thrust,
                                               'mass': self.playership.engine.mass}}))

                self.after = pygame.time.get_ticks()

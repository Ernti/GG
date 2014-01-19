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

        self.now = pygame.time.get_ticks()
        self.after = pygame.time.get_ticks()

    def eventtest(self, uevent):

        self.uevent = uevent

    def move(self):

        self.playership.scale_x = math.cos(math.radians(self.playership.angle))
        self.playership.scale_y = math.sin(math.radians(self.playership.angle))

        self.playership.velocity_x = (self.playership.speed
                                      * self.playership.scale_x)
        self.playership.velocity_y = (self.playership.speed
                                      * self.playership.scale_y)

        # if self.playership.target != (self.playership.x, self.playership.y):



        # print(self.x, self.y)

        if self.uevent is not None:

            if self.uevent.w == True:

                # print('test')

                self.playership.x = self.playership.x \
                                    + self.playership.velocity_x
                self.playership.y = self.playership.y \
                                    + self.playership.velocity_y

                self.now = pygame.time.get_ticks()
                # print(self.now)

                if self.after < (self.now - 100):

                    pygame.event.post(pygame.event.Event(26, {'type': 'playermoved',
                                                              'soid': self.playership.id,
                                                              'x': self.playership.x,
                                                              'y': self.playership.y}))
                    self.after = pygame.time.get_ticks()

                # self.y -= 10

                # self.rect = self.rect.move(0, -1)

            if self.uevent.a == True:

                # self.x -= 10

                self.playership.angle += 1

                # self.rect = self.rect.move(-1, 0)

#            if self.uevent.s == True:
#
#                #self.y += 10
#
#                # self.rect = self.rect.move(0, 1)

            if self.uevent.d == True:

                # self.x += 10

                self.playership.angle -= 1

                # self.rect = self.rect.move(1, 0)
#            pygame.event.post(pygame.event.Event(26, {'type': 'playermoved',
#                                                 'soid': self.id,
#                                                 'x': self.x,
#                                                 'y': self.y}))

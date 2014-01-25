'''
Created on 9 Dec 2013

@author: tore
'''

import math

import pygame.event

from gg.GGspaceship import SpaceShip


class UserEvents(object):

    def __init__(self):

        self.lmsbtn = False
        self.rmsbtn = False
        self.target = None
        self.lock = False
        self.swdwn = False
        self.swup = False


class Events(object):

    def __init__(self, ggci, render):

        self.ggci = ggci
        self.uevents = UserEvents()
        self.player = self.ggci.player
        self.ss = self.player.playership
        self.render = render
        self.running = True

    def eventLoop(self):

        for event in pygame.event.get([pygame.QUIT,
                                       pygame.KEYDOWN,
                                       pygame.KEYUP,
                                       pygame.USEREVENT,
                                       pygame.MOUSEBUTTONDOWN,
                                       pygame.MOUSEBUTTONUP,
                                       pygame.MOUSEMOTION,
                                       pygame.VIDEORESIZE]):

            if event.type == pygame.QUIT:

                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.dict['button'] == 1:
                    self.uevents.lmsbtn = True
                    print('lmsbtn True')

                if event.dict['button'] == 3:

                    self.uevents.rmsbtn = True
                    print('Rmsbtn True')

                if event.dict['button'] == 5:
                    self.uevents.swdwn = True
                    if self.player.z > 0:
                        self.player.z -= 1
                    print('true')

                if event.dict['button'] == 4:
                    self.uevents.swup = True
                    if self.player.z < 50:
                        self.player.z += 1
                    print('true')

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    self.uevents.lmsbtn = False
                    print('lmsbtn False')

                if event.dict['button'] == 3:

                    self.uevents.rmsbtn = False

                if event.dict['button'] == 5:
                    self.uevents.swdwn = False
                    print('False')

                if event.dict['button'] == 4:
                    self.uevents.swup = False
                    print('False')

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_o:
                    self.ss.oxygen = self.ss.oxygen - 1

                elif event.key == pygame.K_F11:

                    if self.render.fullscreen == True:
                        self.render.fullscreen = False
                        self.render.screen = pygame.display. \
                        set_mode(self.render.size,
                                pygame.RESIZABLE)

                    else:
                        self.render.fullscreen = True
                        self.render.screen = pygame.display. \
                        set_mode(self.render.fsres,
                                pygame.FULLSCREEN |
                                pygame.HWSURFACE |
                                pygame.DOUBLEBUF)

                elif event.key == pygame.K_SPACE:
                    if self.uevents.lock == True:

                        self.uevents.lock = False
                    else:

                        self.uevents.lock = True

                elif event.key == pygame.K_m:
                    self.player.playership.mass += 1
                    maxspeed = math.log((0.001 * self.player.playership.mass
                                         ** 1.08)
                            / self.player.playership.thrust, 0.85)
                    print(self.player.playership.mass,
                          self.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_n:
                    self.player.playership.mass -= 1
                    maxspeed = math.log((0.001 * self.player.playership.mass
                                         ** 1.08)
                            / self.player.playership.thrust, 0.85)
                    print(self.player.playership.mass,
                          self.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_k:
                    self.player.playership.thrust += 1
                    maxspeed = math.log((0.001 * self.player.playership.mass
                                         ** 1.08)
                            / self.player.playership.thrust, 0.85)
                    print(self.player.playership.mass,
                          self.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_j:
                    self.player.playership.thrust -= 1
                    maxspeed = math.log((0.001 * self.player.playership.mass
                                         ** 1.08)
                            / self.player.playership.thrust, 0.85)
                    print(self.player.playership.mass,
                          self.player.playership.thrust, maxspeed)

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    self.uevents.w = False

                elif event.key == pygame.K_a:
                    self.uevents.a = False

                elif event.key == pygame.K_s:
                    self.uevents.s = False

                elif event.key == pygame.K_d:
                    self.uevents.d = False

            elif event.type == pygame.USEREVENT:

                data = event.dict
                if data['type'] == 'QUIT':

                    self.running = False

                elif data['type'] == 'newspaceobject':

                    if data['spaceobjecttype'] == 'ss':

                        spaceship = SpaceShip(data['soid'],
                                              data['x'],
                                              data['y'])
                        self.ggci.objectlist.addObject(spaceship)

                elif data['type'] == 'spaceobjectmoved':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid']:

                            objects.x = data['x']
                            objects.y = data['y']
                            objects.scale_x = data['scale_x']
                            objects.scale_y = data['scale_y']
                            objects.speed = data['speed']
                            objects.angle = data['r']

            if self.uevents.lmsbtn == True:

                if event.type == pygame.MOUSEMOTION:

                    if self.uevents.lock == True:

                        self.uevents.lock = False

                    self.player.x += ((event.rel[0] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[0] / 100)))
                    self.player.y -= ((event.rel[1] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[1] / 100)))

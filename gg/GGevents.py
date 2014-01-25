'''
Created on 9 Dec 2013

@author: tore
'''

import math

import pygame.event

from gg.GGspaceship import SpaceShip


class UserEvents(object):

    def __init__(self):

        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.lmsbtn = False
        self.rmsbtn = False
        self.swdwn = False
        self.swup = False


class Events(object):

    def __init__(self, ggci, ss, sg, render):

        self.ggci = ggci
        self.uevents = UserEvents()
        self.ss = ss
        self.player = self.ggci.player
        self.sg = sg
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

                if event.dict['button'] == 5:
                    self.uevents.swdwn = True
                    if self.ggci.player.z > 0:
                        self.ggci.player.z -= 1
                    print('true')

                if event.dict['button'] == 4:
                    self.uevents.swup = True
                    if self.ggci.player.z < 50:
                        self.ggci.player.z += 1
                    print('true')

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    self.uevents.lmsbtn = False
                    print('lmsbtn False')

                if event.dict['button'] == 3:
                    target = pygame.mouse.get_pos()

                    self.ggci.player.target = (self.player.x + (((target[0]
                                            - self.ggci.ggdata.screenwidth / 2)
                                            / self.ggci.ggdata.screenwidth * 2)
                                            * ((math.tan(math.radians(45 / 2))
                                            * (self.ggci.ggdata.screenwidth
                                            / self.ggci.ggdata.screenheight))
                                            * (10 + self.ggci.player.z))),

                                            (self.player.y + (-(target[1]
                                            - self.ggci.ggdata.screenheight / 2)
                                            / self.ggci.ggdata.screenheight * 2)
                                            * (math.tan(math.radians(45 / 2))
                                            * (10 + self.ggci.player.z))))

                    print(self.ggci.player.target)

                    print('Rmsbtn True')
                    print((self.ggci.player.x, self.ggci.player.y))

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

                elif event.key == pygame.K_w:
                    self.uevents.w = True

                elif event.key == pygame.K_a:
                    self.uevents.a = True

                elif event.key == pygame.K_s:
                    self.uevents.s = True

                elif event.key == pygame.K_d:
                    self.uevents.d = True

                elif event.key == pygame.K_m:
                    self.ggci.player.playership.mass += 1
                    maxspeed = math.log((0.001 * self.ggci.player.playership.mass ** 1.08)
                            / self.ggci.player.playership.thrust, 0.85)
                    print(self.ggci.player.playership.mass, self.ggci.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_n:
                    self.ggci.player.playership.mass -= 1
                    maxspeed = math.log((0.001 * self.ggci.player.playership.mass ** 1.08)
                            / self.ggci.player.playership.thrust, 0.85)
                    print(self.ggci.player.playership.mass, self.ggci.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_k:
                    self.ggci.player.playership.thrust += 1
                    maxspeed = math.log((0.001 * self.ggci.player.playership.mass ** 1.08)
                            / self.ggci.player.playership.thrust, 0.85)
                    print(self.ggci.player.playership.mass, self.ggci.player.playership.thrust, maxspeed)

                elif event.key == pygame.K_j:
                    self.ggci.player.playership.thrust -= 1
                    maxspeed = math.log((0.001 * self.ggci.player.playership.mass ** 1.08)
                            / self.ggci.player.playership.thrust, 0.85)
                    print(self.ggci.player.playership.mass, self.ggci.player.playership.thrust, maxspeed)

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

                    self.player.x += ((event.rel[0] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[0] / 100)))
                    self.player.y -= ((event.rel[1] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[1] / 100)))

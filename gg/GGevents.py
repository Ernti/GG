'''
Created on 9 Dec 2013

@author: tore
'''

import math

import pygame.event
from gg.GGbullet import Bullet

from gg.GGspaceship import SpaceShip


class UserEvents(object):

    def __init__(self):

        self.lmsbtn = False
        self.rmsbtn = False
        self.target = None
        self.lock = False
        self.swdwn = False
        self.swup = False

        self.clickedwindow = None


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
                    print(event.dict['pos'])
                    for window in self.ggci.objectlist.windowlist:
                        print((window.posx, window.posy), ((window.posx + window.width), (window.posy + window.height)))
                        if event.dict['pos'] > (window.posx, window.posy) and event.dict['pos'] < ((window.posx + window.width),(window.posy + window.height)):
                            self.uevents.clickedwindow = window
                            print(window)
                    self.uevents.lmsbtn = True
                    print('lmsbtn True')

                if event.dict['button'] == 3:

                    self.uevents.rmsbtn = True
                    print('Rmsbtn True')

                if event.dict['button'] == 4:
                    self.uevents.swdwn = True
                    if self.player.z > 0:
                        self.player.z -= 1
                    print('true')

                if event.dict['button'] == 5:
                    self.uevents.swup = True
                    if self.player.z < 100:
                        self.player.z += 1
                    print('true')

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    if self.uevents.clickedwindow is not None:
                        self.uevents.clickedwindow = None
                    self.uevents.lmsbtn = False
                    print('lmsbtn False')

                if event.dict['button'] == 3:

                    self.uevents.rmsbtn = False

                if event.dict['button'] == 4:
                    self.uevents.swdwn = False
                    print('False')

                if event.dict['button'] == 5:
                    self.uevents.swup = False
                    print('False')

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.ggci.chat.addLine("test")

                elif event.key == pygame.K_KP_ENTER:
                    self.ggci.chat.addLine("test2")

                elif event.key == pygame.K_ESCAPE:
                    if self.ggci.menuwindow.visible is False:
                        self.ggci.menuwindow.show()
                    else:
                        self.ggci.menuwindow.hide()

                elif event.key == pygame.K_s:
                    if self.ggci.statuswindow.visible is False:
                        self.ggci.statuswindow.show()
                    else:
                        self.ggci.statuswindow.hide()

                elif event.key == pygame.K_o:
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

                elif event.key == pygame.K_q:

                    pygame.event.post(pygame.event.Event(
                                            26, {'type': 'playershot',
                                            'x': self.player.playership.x,
                                            'y': self.player.playership.y,
                                            'speed': 10,
                                            'r': self.player.playership.angle}))

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

                elif event.key == pygame.K_d:
                    self.uevents.d = False

            elif event.type == pygame.USEREVENT:

                data = event.dict
                if data['type'] == 'QUIT':

                    self.running = False

                if data['type'] == 'removespaceobject':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid']:

                            self.ggci.objectlist.removeObject(objects)

                if data['type'] == 'spaceobjectmoved':

                    exists = False

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid']:

                            # TODO: Lag Optimization

                            exists = True

                            if data['x'] > objects.x + 1 or data['x'] < objects.x - 1:
                                objects.x = data['x']
                            if data['y'] > objects.y + 1 or data['y'] < objects.y - 1:
                                objects.y = data['y']
                            #objects.scale_x = data['scale_x']
                            #objects.scale_y = data['scale_y']
                            #objects.speed = data['speed']
                            #objects.angle = data['r']
                            objects.target = data['target']

                    if exists == False:

                        spaceship = SpaceShip(data, self.ggci)
                        spaceship.scale_x = data['scale_x']
                        spaceship.scale_y = data['scale_y']
                        spaceship.speed = data['speed']
                        spaceship.angle = data['r']
                        spaceship.target = data['target']
                        self.ggci.objectlist.addObject(spaceship)

                if data['type'] == 'sendchatmessage':

                    self.ggci.chat.chat.append(data['message'])

                if data['type'] == 'playershot':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid'] and objects.type == "ss":
                            objects.weapon.shoot(data)

            if self.uevents.lmsbtn == True:

                if event.type == pygame.MOUSEMOTION:

                    if self.uevents.clickedwindow == None:

                        if self.uevents.lock == True:

                            self.uevents.lock = False

                        self.player.x += ((event.rel[0] / 100)
                                        + ((self.player.z / 10)
                                            * (event.rel[0] / 100)))
                        self.player.y -= ((event.rel[1] / 100)
                                        + ((self.player.z / 10)
                                            * (event.rel[1] / 100)))

                    else:

                        self.uevents.clickedwindow.posx += event.rel[0]
                        self.uevents.clickedwindow.posy += event.rel[1]

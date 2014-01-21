'''
Created on 9 Dec 2013

@author: tore
'''

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
                    self.ggci.player.target = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
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

            if self.uevents.lmsbtn == True:

                if event.type == pygame.MOUSEMOTION:

                    self.player.x += ((event.rel[0] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[0] / 100)))
                    self.player.y -= ((event.rel[1] / 100)
                                      + ((self.player.z / 10)
                                         * (event.rel[1] / 100)))

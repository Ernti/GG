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

    def __init__(self, ggci, ss, sg, render, player):

        self.ggci = ggci
        self.uevents = UserEvents()
        self.ss = ss
        self.player = player
        self.sg = sg
        self.render = render
        self.running = True

    def eventLoop(self):

        for event in pygame.event.get([pygame.QUIT, pygame.KEYDOWN,
                                       pygame.KEYUP, pygame.USEREVENT,
                                       25, pygame.MOUSEBUTTONDOWN,
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
                    print('true')

                if event.dict['button'] == 4:
                    self.uevents.swup = True
                    print('true')

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    self.uevents.lmsbtn = False
                    print('lmsbtn False')

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

            elif self.uevents.lmsbtn == True:

                    if event.type == pygame.MOUSEMOTION:

                        self.player.x += event.rel[0]
                        self.player.y += event.rel[1]

                        print(event.rel)

            elif event.type == 25:

                print('tick')

                for objects in self.ggci.objectlist.objectlist:

                        objects.move()

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

            elif event.type == pygame.VIDEORESIZE:
                self.ss.oxygen = event.w

                if(event.w > 640):
                    self.render.size = self.render.width, self.render.height = (event.w, int(event.w / 16 * 9))
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)

                else:
                    self.render.size = (640, 360)
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)


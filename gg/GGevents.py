'''
Created on 9 Dec 2013

@author: tore
'''

import pygame.event


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

    def __init__(self, ss, sg, render):

        self.uevents = UserEvents()
        self.ss = ss
        self.sg = sg
        self.render = render
        self.running = True

    def eventLoop(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.dict['button'] == 5:
                    self.uevents.swdwn = True
                    print('true')

                if event.dict['button'] == 4:
                    self.uevents.swup = True
                    print('true')

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

            elif event.type == 25:

                print('tick')
                for objects in self.sg.go.objects:

                        objects.move()

            elif event.type == pygame.USEREVENT:

                if event.data == "QUIT":

                    self.running = False

            elif event.type == pygame.VIDEORESIZE:
                self.ss.oxygen = event.w

                if(event.w > 640):
                    self.render.size = (event.w, int(event.w / 16 * 9))
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)

                else:
                    self.render.size = (640, 360)
                    self.render.screen = pygame.display. \
                    set_mode(self.render.size,
                            pygame.RESIZABLE)

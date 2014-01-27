'''
Created on 11 Dec 2013

@author: tore
'''
import os.path

import time

import pygame

from gg.GGcoreinterface import GGCI
from gg.GGevents import Events
from gg.GGrender import Render
from gg.GGspaceship import SpaceShip


class GGcore(object):

    def __init__(self):

        pygame.init()
        self.ggci = GGCI()
        self.ss = SpaceShip(-1, 0, 0, self.ggci)
        self.ggci.player.playership = self.ss
        self.ggci.objectlist.addObject(self.ss)
        self.render = Render(self.ggci)
        self.events = Events(self.ggci, self.render)
        self.clock = pygame.time.Clock()

        self.ggci.player.eventtest(self.events.uevents)

        # GAMETICK = 25
        # pygame.event.Event(GAMETICK)
        # pygame.time.set_timer(GAMETICK, 1000)

    def gameLoop(self):

        self.test = 0
        self.test2 = 0
        while self.events.running:

            self.events.eventLoop()
            self.clock.tick()

            self.ggci.player.move()

            self.test += 1
            self.test1 = self.test2
            self.test2 = int(time.time())
            if self.test2 > self.test1:
                self.fps = self.test
                self.test = 0
                print(self.fps, " fps")
                self.ggci.speed = int(self.ggci.player.playership.speed * 3.6)

            self.render.render()

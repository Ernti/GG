'''
Created on 11 Dec 2013

@author: tore
'''

import pygame

from gg.GGcoreinterface import GGCI
from gg.GGevents import Events
from gg.GGgrid import SpaceGrid
from gg.GGrender import Render
from gg.GGspaceship import SpaceShip
import time


class GGcore(object):

    def __init__(self):

        pygame.init()
        self.ggci = GGCI()
        self.render = Render(self.ggci)
        self.ss = SpaceShip(-1, 0, 0, self.ggci)
        self.sg = SpaceGrid(0, 0)
        self.ggci.objectlist.addObject(self.ss)
        self.events = Events(self.ggci, self.ss, self.sg, self.render)
        self.clock = pygame.time.Clock()

        self.ss.eventtest(self.events.uevents)

        GAMETICK = 25
        pygame.event.Event(GAMETICK)
        pygame.time.set_timer(GAMETICK, 10)

    def gameLoop(self):

        self.test = 0
        self.test2 = 0
        while self.events.running:

            self.events.eventLoop()
            self.clock.tick()


            self.test += 1
            self.test1 = self.test2
            self.test2 = int(time.time())
            if self.test2 > self.test1:
                print("ding")
                self.fps = self.test
                self.test = 0
                print(self.fps)

            self.render.render(str(self.ss.oxygen),
                               self.fps, self.sg)

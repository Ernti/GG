'''
Created on 11 Dec 2013

@author: tore
'''

import pygame

from gg.GGevents import Events
from gg.GGgrid import SpaceGrid
from gg.GGplayer import Player
from gg.GGrender import Render
from gg.GGspaceship import SpaceShip


class GGcore(object):

    def __init__(self):

        pygame.init()
        self.render = Render()
        self.ss = SpaceShip()
        self.player = Player()
        self.sg = SpaceGrid(0, 0)
        self.sg.addObject(self.ss)
        self.events = Events(self.ss, self.sg, self.render, self.player)
        self.clock = pygame.time.Clock()

        self.ss.eventtest(self.events.uevents)

        GAMETICK = 25
        pygame.event.Event(GAMETICK)
        pygame.time.set_timer(GAMETICK, 100)

    def gameLoop(self):

        while self.events.running:

            self.events.eventLoop()
            self.clock.tick()

            self.render.render(str(self.ss.oxygen),
                               str(int(self.clock.get_fps())),
                               self.sg, self.player)

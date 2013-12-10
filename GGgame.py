'''
Created on 5 Dec 2013

@author: tore
'''

import pygame

from gg.GGevents import Events
from gg.GGgrid import SpaceGrid
from gg.GGrender import Render
from gg.GGspaceship import SpaceShip


pygame.init()
render = Render()
ss = SpaceShip()
events = Events(ss, render)
clock = pygame.time.Clock()

sg = SpaceGrid()
sg.addObject(ss)

ss.eventtest(events.uevents)

while 1:

    events.eventLoop()
    sg.gridLoop()
    clock.tick()

    render.render(str(ss.oxygen), str(int(clock.get_fps())), sg)

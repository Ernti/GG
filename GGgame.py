'''
Created on 5 Dec 2013

@author: tore
'''

import sys

import pygame

from gg.GGrender import Render
from gg.GGspaceship import SpaceShip


pygame.init()
render = Render()
ss = SpaceShip()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                ss.oxygen = ss.oxygen - 1
        elif event.type == pygame.VIDEORESIZE:
            render.size = event.size

    render.render(str(ss.oxygen))

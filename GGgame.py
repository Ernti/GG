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
clock = pygame.time.Clock()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                ss.oxygen = ss.oxygen - 1
            if event.key == pygame.K_F11:
                if render.fullscreen == True:
                    render.fullscreen = False
                    render.screen = pygame.display.set_mode(render.size,
                                                             pygame.RESIZABLE)
                else:
                    render.fullscreen = True
                    render.screen = pygame.display.set_mode(render.fsres,
                                                            pygame.FULLSCREEN |
                                                             pygame.HWSURFACE |
                                                             pygame.DOUBLEBUF)
            if event.key == pygame.K_d:
                ss.ssrect = ss.ssrect.move(2, 0)
        elif event.type == pygame.VIDEORESIZE:
            ss.oxygen = event.w
            if(event.w > 640):
                render.size = (event.w, int(event.w / 16 * 9))
                render.screen = pygame.display.set_mode(render.size,
                                                             pygame.RESIZABLE)
            else:
                render.size = (640, 360)
                render.screen = pygame.display.set_mode(render.size,
                                                             pygame.RESIZABLE)
    clock.tick()

    render.render(str(ss.oxygen), str(int(clock.get_fps())), ss)

'''
Created on 25 Feb 2014

@author: tore
'''
import pygame
from gg.GGbullet import Bullet


class Weapon(object):

    def __init__(self, ss, type, ggci):

        self.ggci = ggci
        self.ss = ss
        self.type = type

    def shoot(self):

        bullet = Bullet({'x': self.ss.x, 'y': self.ss.y, 'r': self.ss.r}, self.ggci)
        self.ggci.objectlist.addObject(bullet)

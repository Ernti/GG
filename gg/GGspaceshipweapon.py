'''
Created on 25 Feb 2014

@author: tore
'''
import pygame
from gg.GGbullet import Bullet


class Weapon(object):

    def __init__(self, type, ggci):

        self.ggci = ggci
        self.type = type

    def shoot(self, data):

        bullet = Bullet(data, self.ggci)
        self.ggci.objectlist.addObject(bullet)

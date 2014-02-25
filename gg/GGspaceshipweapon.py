'''
Created on 25 Feb 2014

@author: tore
'''
from gg.GGbullet import Bullet


class Weapon(object):

    def __init__(self, type, ggci):

        self.ggci = ggci
        self.type = type

    def shoot(self, startpos, angle):

        self.bullet = Bullet(startpos, self.ggci.player.playership.angle + (angle - self.ggci.player.playership.angle),
                             self.ggci)
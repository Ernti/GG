'''
Created on 17 Dec 2013

@author: tore
'''
from gg.GGdata import GGData
from gg.GGobjectlist import ObjectList
from gg.GGplayer import Player


class GGCI(object):

    def __init__(self):

        self.ggdata = GGData()
        self.objectlist = ObjectList()
        self.player = Player(self)
        self.speed = 0

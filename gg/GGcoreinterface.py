'''
Created on 17 Dec 2013

@author: tore
'''
import os.path
import pygame
from gg.GGButtonhandler import Buttonhandler
from gg.GGchat import ChatWindow
from gg.GGdata import GGData
from gg.GGobjectlist import ObjectList
from gg.GGplayer import Player
from gg.GGradar import Radar
from gg.GGtextrender import TextRender
from gg.GGwindowmanager import WindowManager


class GGCI(object):

    def __init__(self):

        self.ggdata = GGData()
        self.objectlist = ObjectList()
        self.player = Player(self)
        self.speed = 0
        self.chat = ChatWindow(self)
        self.textrender = TextRender(self)
        self.radar = Radar(self)

        # self.obj = OBJ(os.path.join(".", "gg", "data", "objects", "ship.obj"), swapyz=False)

    def wmInit(self):

        self.wm = WindowManager(self)
        self.buttonhandler = Buttonhandler(self)

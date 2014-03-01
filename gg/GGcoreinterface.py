'''
Created on 17 Dec 2013

@author: tore
'''
import os.path
from gg.GGchat import ChatWindow
from gg.GGdata import GGData
from gg.GGobjectlist import ObjectList
from gg.GGplayer import Player
from gg.GGradar import Radar
from gg.GGtextrender import TextRender
from gg.GGwindow import Window


class GGCI(object):

    def __init__(self):

        self.ggdata = GGData()
        self.objectlist = ObjectList()
        self.player = Player(self)
        self.speed = 0
        self.chat = ChatWindow(self)
        self.textrender = TextRender(self)
        self.radar = Radar(self)

        self.menuwindow = Window("Menu", self.ggdata.screenwidth / 2 - 50,
                                 self.ggdata.screenheight / 2 - 100, 100, 200, self)
        self.statuswindow = Window("Status", 10, 10, 200, 400, self)
        self.statuswindow.text.append("test")
        self.statuswindow.text.append("test2")
        self.statuswindow.text.append("test3")

        # self.obj = OBJ(os.path.join(".", "gg", "data", "objects", "ship.obj"), swapyz=False)

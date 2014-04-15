'''
Created on 15 Apr 2014

@author: tore
'''

from gg.GGwindow import Window
from gg.GGwindowbutton import WindowButton
from gg.GGwindowlist import WindowList


class WindowManager(object):

    def __init__(self, ggci):

        self.ggci = ggci

        self.menuwindow = Window("Menu", self.ggci.ggdata.screenwidth / 2 - 50,
                                 self.ggci.ggdata.screenheight / 2 - 100, 100, 200, self.ggci)
        self.menuwindow.buttons.append(WindowButton(self.menuwindow, "Exit", 10, 170, 80, 20, 'quit'))

        self.statuswindow = Window("Status", 10, 10, 200, 400, self.ggci)
        self.statuswindow.text.append("test")
        self.statuswindow.text.append("test2")
        self.statuswindow.text.append("test3")

        self.inventorywindow = Window("Inventory", self.ggci.ggdata.screenwidth - 450,
                                      self.ggci.ggdata.screenheight - 350, 400, 300, self.ggci)
        self.inventorywindow.lists.append(WindowList(self.inventorywindow, self.ggci.player.playership.inventory, 5, 25,
                                                     390, 270, int(270 / self.ggci.ggdata.screenheight / 60)))
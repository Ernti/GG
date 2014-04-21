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

        #     __  ___                     _         __
        #    /  |/  /__ ___  __ ___    __(_)__  ___/ /__ _    __
        #   / /|_/ / -_) _ \/ // / |/|/ / / _ \/ _  / _ \ |/|/ /
        #  /_/  /_/\__/_//_/\_,_/|__,__/_/_//_/\_,_/\___/__,__/
        #

        self.menuwindow = Window("Menu",
                                 self.ggci.ggdata.screenwidth / 2 - 50,
                                 self.ggci.ggdata.screenheight / 2 - 100,
                                 100,
                                 200,
                                 self.ggci)
        self.menuwindow.buttons.append(WindowButton(self.menuwindow,
                                                    "Exit",
                                                    10,
                                                    170,
                                                    80,
                                                    20,
                                                    'quit'))

        #     ______       __                 _         __
        #    / __/ /____ _/ /___ ______    __(_)__  ___/ /__ _    __
        #   _\ \/ __/ _ `/ __/ // (_-< |/|/ / / _ \/ _  / _ \ |/|/ /
        #  /___/\__/\_,_/\__/\_,_/___/__,__/_/_//_/\_,_/\___/__,__/
        #

        self.statuswindow = Window("Status",
                                   10,
                                   10,
                                   200,
                                   400,
                                   self.ggci)
        self.statuswindow.text.append("test")
        self.statuswindow.text.append("test2")
        self.statuswindow.text.append("test3")

        #     ____                  __                       _         __
        #    /  _/__ _  _____ ___  / /____  ______ ___    __(_)__  ___/ /__ _    __
        #   _/ // _ \ |/ / -_) _ \/ __/ _ \/ __/ // / |/|/ / / _ \/ _  / _ \ |/|/ /
        #  /___/_//_/___/\__/_//_/\__/\___/_/  \_, /|__,__/_/_//_/\_,_/\___/__,__/
        #                                     /___/

        self.inventorywindow = Window("Inventory",
                                      self.ggci.ggdata.screenwidth - 450,
                                      self.ggci.ggdata.screenheight - 350,
                                      400,
                                      300,
                                      self.ggci)
        self.inventorywindow.lists.append(WindowList(self.inventorywindow,
                                                     self.ggci.player.playership.inventory,
                                                     5,
                                                     25,
                                                     390,
                                                     270,
                                                     int(270 / self.ggci.ggdata.screenheight / 60)))

        #     ______    _ ____          _         __
        #    / __/ /__ (_) / /___    __(_)__  ___/ /__ _    __
        #   _\ \/  '_// / / (_-< |/|/ / / _ \/ _  / _ \ |/|/ /
        #  /___/_/\_\/_/_/_/___/__,__/_/_//_/\_,_/\___/__,__/
        #

        self.skillswindow = Window("Skills",
                                   50,
                                   self.ggci.ggdata.screenheight - 450,
                                   self.ggci.textrender.statchar[49][1] * 25 + 10,
                                   self.ggci.textrender.statchar[49][2] * 30 + 30,
                                   self.ggci)
        self.skillswindow.lists.append(WindowList(self.skillswindow,
                                                  self.ggci.player.skills,
                                                  5,
                                                  25,
                                                  self.ggci.textrender.statchar[49][1] * 25,
                                                  self.ggci.textrender.statchar[49][2] * 30,
                                                  30))
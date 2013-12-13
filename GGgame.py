'''
Created on 5 Dec 2013

@author: tore
'''

import sys

from gg.GGcore import GGcore
from net.connection import Network
from gg.GGlauncher import GGlauncher

launcher = GGlauncher(GGlauncher.launcherScreen)
launcher.launcherLoop()

net = Network()
net.connect()


if net.connected == True:

    game = GGcore()
    game.gameLoop()

net.close()
sys.exit()

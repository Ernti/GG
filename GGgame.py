'''
Created on 5 Dec 2013

@author: tore
'''

import sys

from gg.GGcore import GGcore
from net.connection import Network
from gg.GGlauncher import GGlauncher

launcher = GGlauncher()
login = launcher.launcherLoop()

net = Network(login)
net.connect()


if net.connected == True:

    game = GGcore()
    net.sendthread.start()
    try:
        game.gameLoop()
    except KeyboardInterrupt:
        print("stopping...")
        game.events.running = False


net.close()
sys.exit()

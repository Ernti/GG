'''
Created on 5 Dec 2013

@author: tore
'''

import os
import sys

from gg.GGcore import GGcore
from gg.GGsplashscreen import SplashScreen
from net.connection import Network
from gg.GGlauncher import GGlauncher

os.environ['SDL_VIDEO_CENTERED'] = '1'

launcher = GGlauncher()
login = launcher.launcherLoop()

SplashScreen()

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

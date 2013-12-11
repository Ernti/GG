'''
Created on 5 Dec 2013

@author: tore
'''

import sys

from gg.GGcore import GGcore
from net.connection import Network


net = Network()
net.connect()


if net.connected == True:

    game = GGcore()
    game.gameLoop()

net.close()
sys.exit()

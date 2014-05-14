'''
Created on 11 Dec 2013

@author: tore
'''
import os.path
import random

import time

import pygame

from gg.GGchat import ChatWindow
from gg.GGcollisiondetector import CollisionDetektor
from gg.GGcoreinterface import GGCI
from gg.GGevents import Events
from gg.GGitem import Item
from gg.GGitemobject import Itemobject
from gg.GGplanet import Planet
from gg.GGrender import Render
from gg.GGspaceship import SpaceShip
from gg.GGobjloader import *


class GGcore(object):

    def __init__(self):

        pygame.init()
        self.ggci = GGCI()
        self.ss = SpaceShip({'soid': -1, 'x': 0, 'y': 0,
                             'engine': {'type': "Electromotor", 'thrust': 10, 'mass': 100}}, self.ggci)
        self.ggci.player.playership = self.ss
        self.ggci.objectlist.addObject(self.ss)

        testitem1 = Item({'name': 'Scrap', 'id': 1, 'type': 'scrap', 'amount': 7})
        self.ggci.player.playership.inventory.append(testitem1)

        self.ggci.wmInit()
        self.render = Render(self.ggci)
        self.events = Events(self.ggci, self.render)

        self.ggci.player.eventtest(self.events.uevents)

        testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
        self.ggci.objectlist.addObject(testitem)
        testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
        self.ggci.objectlist.addObject(testitem)
        testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
        self.ggci.objectlist.addObject(testitem)
        testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
        self.ggci.objectlist.addObject(testitem)
        testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
        self.ggci.objectlist.addObject(testitem)

        testplanet = Planet(1337, 0, 1000, 1000, 0.0001, self.ggci)
        self.ggci.objectlist.addObject(testplanet)
        testplanet = Planet(1338, 0, 1000, 750, 0.001, self.ggci)
        self.ggci.objectlist.addObject(testplanet)
        testplanet = Planet(1339, 0, 1000, 1250, 0.0003, self.ggci)
        self.ggci.objectlist.addObject(testplanet)
        testplanet = Planet(1340, 0, 1000, 1500, 0.00001, self.ggci)
        self.ggci.objectlist.addObject(testplanet)

    def gameLoop(self):

        self.test = 0
        self.test2 = 0
        while self.events.running:

            self.events.eventLoop()

            self.ggci.player.move()
            for objects in self.ggci.objectlist.objectlist:
                if objects.id is not -1:
                    objects.action()

            self.test += 1
            self.test1 = self.test2
            self.test2 = int(time.time())
            if self.test2 > self.test1:
                self.fps = self.test
                self.test = 0
                print(self.fps, " fps")
                self.ggci.speed = int(self.ggci.player.playership.speed * 3.6)

            CollisionDetektor(self.ggci)

            self.render.render()

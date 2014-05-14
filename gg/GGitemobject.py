'''
Created on 14 Apr 2014

@author: tore
'''
import math
import random
from OpenGL.GL import *

from gg.GGitem import Item


class Itemobject(object):

    def __init__(self, data, ggci):

        self.ggci = ggci
        self.id = data['soid']
        self.type = "item"

        self.item = Item(data['item'])

        self.x = data['x']
        self.y = data['y']

        self.lived = data['lived']
        self.alive = data['alive']

        self.vertex = [[2, 2, 0], [-2, -2, 0]]
        self.r = 0

    def action(self):

        if self.lived > self.alive:
            self.ggci.objectlist.removeObject(self)

        x = abs(self.ggci.player.playership.x - self.x)
        y = abs(self.ggci.player.playership.y - self.y)
        a = math.sqrt(x**2+y**2)

        if a < 2:
            newitem = True
            for item in self.ggci.player.playership.inventory:
                if item.name == self.item.name and item.type == self.item.type:
                    self.ggci.player.playership.inventory[self.ggci.player.playership.inventory.index(item)].amount \
                        += self.item.amount
                    newitem = False

            if newitem is True:
                self.ggci.player.playership.inventory.append(self.item)
            self.ggci.chat.chat.append("You get " + str(self.item.amount) + ' ' + self.item.name + '!')
            self.ggci.objectlist.removeObject(self)

            testitem = Itemobject({'soid': 123, 'x': random.randint(-100, 100), 'y': random.randint(-100, 100), 'lived': 0, 'alive': 100, 'item': {'name': 'Scrap', 'id': 1,
                                                                                      'type': 'scrap', 'amount': 7}}, self.ggci)
            self.ggci.objectlist.addObject(testitem)

    def render(self):

        glColor3f(0.2, 0.2, 0.2)
        r = 0.5
        angle = 0
        glBegin(GL_POLYGON)
        while angle < 2 * math.pi:
            glVertex3f(self.ggci.player.x + self.x + r * math.cos(angle),
                       self.ggci.player.y + self.y + r * math.sin(angle),
                       0 - self.ggci.player.z)
            angle += 0.1
        glEnd()

    def debugRender(self):

        glColor(0, 0.8, 0.2)

        glBegin(GL_LINE_LOOP)
        glVertex3f(self.collisionbox[0] + self.x + self.ggci.player.x,
                   self.collisionbox[2] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[1] + self.x + self.ggci.player.x,
                   self.collisionbox[2] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[1] + self.x + self.ggci.player.x,
                   self.collisionbox[3] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glVertex3f(self.collisionbox[0] + self.x + self.ggci.player.x,
                   self.collisionbox[3] + self.y + self.ggci.player.y,
                   0 - self.ggci.player.z)
        glEnd()



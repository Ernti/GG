'''
Created on 17 Dec 2013

@author: tore
'''


class ObjectList(object):

    def __init__(self):
        self.objectlist = []
        self.windowlist = []

    def addObject(self, listobject):

        self.objectlist.append(listobject)

    def removeObject(self, listobject):

        self.objectlist.remove(listobject)

    def addWindow(self, listobject):

        self.windowlist.append(listobject)

    def removeWindow(self, listobject):

        self.windowlist.remove(listobject)

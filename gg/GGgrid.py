'''
Created on 9 Dec 2013

@author: tore
'''


class SpaceGrid(object):

    def __init__(self):

        self.go = GridObjects()
        self.x = 0
        self.y = 0

    def gridLoop(self):

        for objects in self.go.objects:

            objects.move()

    def addObject(self, sobject):

        self.go.objects.append(sobject)


class GridObjects(object):

    def __init__(self,):

        self.objects = []

'''
Created on 9 Dec 2013

@author: tore
'''


class SpaceGrid(object):

    def __init__(self):

        self.go = GridObjects()
        self.x = 0
        self.y = 0
        self.z = 1

    def gridLoop(self, events):

        for objects in self.go.objects:

            objects.move()

        if events.uevents.swdwn == True:

            print('test')
            self.z = self.z + 0.1
            events.uevents.swdwn = False

        elif events.uevents.swup == True:

            print('test')
            self.z = self.z - 0.1
            events.uevents.swup = False

    def addObject(self, sobject):

        self.go.objects.append(sobject)


class GridObjects(object):

    def __init__(self,):

        self.objects = []

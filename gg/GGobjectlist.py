'''
Created on 17 Dec 2013

@author: tore
'''


class ObjectList(object):

    def __init__(self):
        self.objectlist = []

    def addObject(self, listobject):

        self.objectlist.append(listobject)

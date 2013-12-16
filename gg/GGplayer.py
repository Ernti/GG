'''
Created on 16 Dec 2013

@author: tore
'''
from gg.GGgridobject import GridObject


class Player(GridObject):

    def __init__(self):

        super(GridObject, self).__init__()

        self.x = 640
        self.y = 360

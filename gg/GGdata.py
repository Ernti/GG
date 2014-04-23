'''
Created on 24 Jan 2014

@author: tore
'''


class GGData:  # General Game Data the User should be able to change.

    def __init__(self):

        self.screensize = self.screenwidth, self.screenheight = 1280, 720
        self.fullscreen = False

        self.chatlength = 5

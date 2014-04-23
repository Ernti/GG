'''
Created on 1 Mar 2014

@author: tore
'''

import pygame


class Buttonhandler(object):

    def __init__(self, ggci):

        self.ggci = ggci

    def handle(self, dict):

        if dict['action'] == 'quit':

            pygame.event.post(pygame.event.Event(pygame.QUIT))

        elif dict['action'] == 'options':

            self.ggci.wm.optionswindow.show()
            self.ggci.wm.menuwindow.hide()

        elif dict['action'] == 'fullscreen':

            if self.ggci.ggdata.fullscreen is True:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'type': 'windowed'}))
                self.ggci.ggdata.fullscreen = False
            else:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'type': 'fullscreen'}))
                self.ggci.ggdata.fullscreen = True
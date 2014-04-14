'''
Created on 1 Mar 2014

@author: tore
'''

import pygame


class Buttonhandler(object):

    def handle(self, dict):

        if dict['action'] == 'quit':

            pygame.event.post(pygame.event.Event(pygame.QUIT))
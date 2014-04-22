'''
Created on 28 Jan 2014

@author: tore
'''
import pygame


class ChatWindow(object):

    def __init__(self, ggci):

        self.ggci = ggci
        self.chat = []
        self.input = False
        self.inputstring = ""
        self.chat.append("Wilkommen!")

    def addLine(self, message):

        pygame.event.post(pygame.event.Event(
                                    26,{
                                        'type': 'sendchatmessage',
                                        'message': message
                                    }))
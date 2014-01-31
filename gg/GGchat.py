'''
Created on 28 Jan 2014

@author: tore
'''



class ChatWindow(object):

    def __init__(self, ggci):

        self.ggci = ggci
        self.ggci.chat.append("Wilkommen!")

    def addLine(self, message):

        self.ggci.chat.append(message)
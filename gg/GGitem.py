'''
Created on 14 Apr 2014

@author: tore
'''


class Item(object):

    def __init__(self, data):

        self.name = data['name']
        self.id = data['id']
        self.type = data['type']
        self.amount = data['amount']

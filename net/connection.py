'''
Created on 9 Dec 2013

@author: tore
'''

import json
import socket
from threading import Thread

import pygame.event


stop_requested = False


class Network(object):

    def __init__(self):

        self.userdict = {'username': 'testname', 'password': 'iminspace'}
        self.connected = False
        global stop_requested

    def connect(self):

        try:

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('localhost', 4455))
            self.sock.send(json.dumps(self.userdict).encode())
            data = self.sock.recv(1024)
            data_json = json.loads(data.decode())
            if data_json['type'] == 'connected':

                self.connected = True
                print("connected")
                self.recthread = ReceiverThread(self.sock)
                self.sendthread = SenderThread(self.sock)
                self.recthread.start()

            elif data_json['type'] == 'loginerror':

                print("Wrong Username or Password!")

        except KeyboardInterrupt:

            stop_requested = True

        except socket.error:

            print("couldn't connect to server!")

    def close(self):

        print("stopping...")
        if self.connected == True:
            stop_requested = True
            self.recthread._stop()
            self.sendthread._stop()

        self.sock.close()


class ReceiverThread(Thread):

    def __init__(self, socket):

        Thread.__init__(self)
        self.sock = socket
        global stop_requested

    def run(self):
        global stop_requested
        while not stop_requested:
            try:
                data = self.sock.recv(1024)
                print(data.decode())
                data_json = json.loads(data.decode())
                if data_json['type'] == 'shutdown':
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         {'type': 'QUIT'}))
                    stop_requested = True

                    print(data.decode())

                elif data_json['type'] == 'newspaceobject':

                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         data_json))

                elif data_json['type'] == 'spaceobjectmoved':

                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         data_json))

            except socket.error:

                print("Connection Lost!")
                pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                    {'type': 'QUIT'}))
                stop_requested = True


class SenderThread(Thread):

    def __init__(self, socket):

        Thread.__init__(self)
        self.sock = socket
        global stop_requested

    def run(self):
        global stop_requested
        while not stop_requested:
            try:

                for event in pygame.event.get(26):

                    if event.type == 26:

                        self.sock.send(json.dumps(event.dict).encode())
                pygame.time.wait(10)

            except socket.error:

                print("Connection Lost!")
                pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                    {'type': 'QUIT'}))
                stop_requested = True

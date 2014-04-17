'''
Created on 9 Dec 2013

@author: tore
'''

import json
import socket
import re
from threading import Thread

import pygame.event


stop_requested = False


class Network(object):

    def __init__(self, userdict):

        self.hostaddresse = ''
        self.hostport = ''
        self.userdict = userdict
        self.connected = False
        global stop_requested

    def connect(self):

        try:

            hostfile = open('host', 'r')
            for line in hostfile:
                linearry = list(line)
                if linearry[0] == '#':
                    continue

                else:
                    port = False
                    for char in linearry:
                        if char == ":":
                            print("port")
                            port = True
                            continue
                        else:
                            if port == False:
                                self.hostaddresse += char
                                print(self.hostaddresse)
                            else:
                                self.hostport += char
                                print(self.hostport)


            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.hostaddresse, int(self.hostport)))
            self.sock.send(('(' + json.dumps(self.userdict) + ')').encode())
            data = self.sock.recv(1024)
            for match_group in re.finditer("\(([^()]+)\)", data.decode()):

                data_json = json.loads(match_group.group(1))
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
                #print(data.decode())

                for match_group in re.finditer("\(([^()]+)\)", data.decode()):

                    data_json = json.loads(match_group.group(1))
                    if data_json['type'] == 'shutdown':
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                            {'type': 'QUIT'}))
                        stop_requested = True

                        print(data.decode())

                    elif data_json['type'] == 'newspaceobject':

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                            data_json))

                    elif data_json['type'] == 'removespaceobject':

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                            data_json))

                    elif data_json['type'] == 'spaceobjectmoved':

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                            data_json))

                    elif data_json['type'] == 'sendchatmessage':

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                            data_json))

                    elif data_json['type'] == 'playershot':

                        print(data_json)

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

                        self.sock.send(('(' + json.dumps(event.dict) + ')').encode())

                pygame.time.wait(10)

            except socket.error:

                print("Connection Lost!")
                pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                    {'type': 'QUIT'}))
                stop_requested = True

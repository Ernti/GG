'''
Created on 9 Dec 2013

@author: tore
'''

import json
import socket
from threading import Thread

stop_requested = False


class Network(object):

    def __init__(self):

        self.userdict = {'username': 'testname', 'password': 'iminspace'}
        self.connected = False

    def connect(self):

        try:

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('localhost', 4455))
            self.sock.send(json.dumps(self.userdict).encode())
            data = self.sock.recv(1024)
            if data.decode() == "connected":

                self.connected = True
                print("connected")

            conthread = ConnectionThread(self.sock)
            conthread.start()

        except KeyboardInterrupt:

            stop_requested = True

        except socket.error:

            print("couldn't connect to server!")

    def close(self):

        self.sock.close()


class ConnectionThread(Thread):

    def __init__(self, socket):

        Thread.__init__(self)
        self.sock = socket

    def run(self):
        while not stop_requested:
            data = self.sock.recv(1024)
            if data == "shutdown":
                self.sock.close()

            print(data.decode())

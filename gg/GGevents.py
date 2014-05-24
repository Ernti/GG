'''
Created on 9 Dec 2013

@author: tore
'''

import math

import pygame.event
from gg.GGbullet import Bullet
from gg.GGcontextmenu import ContextMenu

from gg.GGspaceship import SpaceShip
from gg.GGtextinput import TextInput
from gg.GGwindowbutton import WindowButton


class UserEvents(object):

    def __init__(self):

        self.lmsbtn = False
        self.rmsbtn = False
        self.target = None
        self.lock = False
        self.swdwn = False
        self.swup = False

        self.clickedwindow = None
        self.chatting = False


class Events(object):

    def __init__(self, ggci, render):

        self.ggci = ggci
        self.uevents = UserEvents()
        self.player = self.ggci.player
        self.ss = self.player.playership
        self.render = render
        self.running = True
        self.ti = TextInput()

    def eventLoop(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

            #-----------------------------------------
            #-----------MOUSEBUTTON-PRESSED-----------
            #-----------------------------------------

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.ggci.contextmenu is not None:
                    if ((event.dict['pos'][0] > self.ggci.contextmenu.posx
                         and event.dict['pos'][1] > self.ggci.contextmenu.posy)
                        and (event.dict['pos'][0] < (self.ggci.contextmenu.posx + self.ggci.contextmenu.width)
                             and event.dict['pos'][1] < (self.ggci.contextmenu.posy + self.ggci.contextmenu.height))):

                        for button in self.ggci.contextmenu.buttons:

                                if ((event.dict['pos'][0] > (self.ggci.contextmenu.posx + button.posx)
                                     and event.dict['pos'][1] > (self.ggci.contextmenu.posy + button.posy))
                                    and (event.dict['pos'][0] < (self.ggci.contextmenu.posx + button.posx + button.width)
                                         and event.dict['pos'][1] < (self.ggci.contextmenu.posy + button.posy + button.height))):


                                    button.action()
                                    self.ggci.contextmenu = None
                                    break
                        continue

                    else:

                        self.ggci.contextmenu = None

                if event.dict['button'] == 1:
                    print(event.dict['pos'])
                    for window in self.ggci.objectlist.windowlist:
                        print((window.posx, window.posy), ((window.posx + window.width), (window.posy + window.height)))
                        if ((event.dict['pos'][0] > window.posx
                             and event.dict['pos'][1] > window.posy)
                            and (event.dict['pos'][0] < (window.posx + window.width)
                                 and event.dict['pos'][1] < (window.posy + window.height))):

                            for button in window.buttons:

                                if ((event.dict['pos'][0] > (window.posx + button.posx)
                                     and event.dict['pos'][1] > (window.posy + button.posy))
                                    and (event.dict['pos'][0] < (window.posx + button.posx + button.width)
                                         and event.dict['pos'][1] < (window.posy + button.posy + button.height))):

                                    button.action()

                            self.uevents.clickedwindow = window
                            print(window)

                    self.uevents.lmsbtn = True
                    print('lmsbtn True')

                if event.dict['button'] == 3:

                    if len(self.ggci.objectlist.windowlist) is 0:
                        self.uevents.rmsbtn = True
                        print('Rmsbtn True')
                    for window in self.ggci.objectlist.windowlist:
                        print((window.posx, window.posy), ((window.posx + window.width), (window.posy + window.height)))
                        if ((event.dict['pos'][0] > window.posx
                             and event.dict['pos'][1] > window.posy)
                            and (event.dict['pos'][0] < (window.posx + window.width)
                                 and event.dict['pos'][1] < (window.posy + window.height))):

                            for list in window.lists:
                                for item in list.list:
                                    if ((event.dict['pos'][0] > window.posx + list.posx
                                         and event.dict['pos'][1] > window.posy + list.posy
                                            + self.ggci.textrender.statchar[49][2] * list.list.index(item))
                                        and (event.dict['pos'][0] < (window.posx + list.posx + list.width)
                                             and event.dict['pos'][1] < window.posy + list.posy
                                                + self.ggci.textrender.statchar[49][2]
                                                + self.ggci.textrender.statchar[49][2] * list.list.index(item))):

                                        contextmenu = ContextMenu(item, event.dict['pos'], self.ggci)
                                        testbuttons = [WindowButton(contextmenu, 'use', 0, 0, 100, self.ggci.textrender.statchar[49][2], 'useitem'),
                                                       WindowButton(contextmenu, 'test', 0, self.ggci.textrender.statchar[49][2], 100, self.ggci.textrender.statchar[49][2], ''),
                                                       WindowButton(contextmenu, 'test', 0, self.ggci.textrender.statchar[49][2] * 2, 100, self.ggci.textrender.statchar[49][2], ''),
                                                       WindowButton(contextmenu, 'test', 0, self.ggci.textrender.statchar[49][2] * 3, 100, self.ggci.textrender.statchar[49][2], '')]
                                        contextmenu.addButtons(testbuttons)
                                        self.ggci.contextmenu = contextmenu

                                        print(item.name)




                        else:

                            self.uevents.rmsbtn = True
                            print('Rmsbtn True')

                if event.dict['button'] == 4:
                    self.uevents.swdwn = True
                    if self.player.z > 0:
                        self.player.z -= 1
                    print('true')

                if event.dict['button'] == 5:
                    self.uevents.swup = True
                    if self.player.z < 100:
                        self.player.z += 1
                    print('true')

            #----------------------------------------
            #----------MOUSEBUTTON-RELEASED----------
            #----------------------------------------

            elif event.type == pygame.MOUSEBUTTONUP:

                if event.dict['button'] == 1:
                    if self.uevents.clickedwindow is not None:
                        self.uevents.clickedwindow = None
                    self.uevents.lmsbtn = False
                    print('lmsbtn False')

                if event.dict['button'] == 3:

                    self.uevents.rmsbtn = False

                if event.dict['button'] == 4:
                    self.uevents.swdwn = False
                    print('False')

                if event.dict['button'] == 5:
                    self.uevents.swup = False
                    print('False')

            #-----------------------------------------
            #---------------KEY-PRESSED---------------
            #-----------------------------------------

            elif event.type == pygame.KEYDOWN:

                if self.ggci.chat.input is False:

                    if event.key == pygame.K_RETURN:
                        self.ggci.chat.input = True

                    elif event.key == pygame.K_KP_ENTER:
                        self.ggci.chat.addLine("test2")

                    elif event.key == pygame.K_ESCAPE:
                        if len(self.ggci.objectlist.windowlist) is 0:
                            self.ggci.wm.menuwindow.show()
                        else:
                            self.ggci.objectlist.windowlist[-1].hide()

                    elif event.key == pygame.K_s:
                        if self.ggci.wm.skillswindow.visible is False:
                            self.ggci.wm.skillswindow.show()
                        else:
                            self.ggci.wm.skillswindow.hide()

                    elif event.key == pygame.K_c:
                        if self.ggci.wm.statuswindow.visible is False:
                            self.ggci.wm.statuswindow.show()
                        else:
                            self.ggci.wm.statuswindow.hide()

                    elif event.key == pygame.K_i:
                        if self.ggci.wm.inventorywindow.visible is False:
                            self.ggci.wm.inventorywindow.show()
                        else:
                            self.ggci.wm.inventorywindow.hide()

                    elif event.key == pygame.K_o:
                        self.ss.oxygen = self.ss.oxygen - 1

                    elif event.key == pygame.K_F11:

                        if self.render.fullscreen == True:
                            self.render.fullscreen = False
                            self.render.screen = pygame.display. \
                            set_mode(self.render.size,
                                    pygame.RESIZABLE)

                        else:
                            self.render.fullscreen = True
                            self.render.screen = pygame.display. \
                            set_mode(self.render.fsres,
                                    pygame.FULLSCREEN |
                                    pygame.HWSURFACE |
                                    pygame.DOUBLEBUF)

                    elif event.key == pygame.K_SPACE:
                        if self.uevents.lock == True:

                            self.uevents.lock = False
                        else:

                            self.uevents.lock = True

                    elif event.key == pygame.K_q:

                        self.player.playership.weapon.shoot()

                        #pygame.event.post(pygame.event.Event(
                        #                        26, {'type': 'playershot',
                        #                        'x': self.player.playership.x,
                        #                        'y': self.player.playership.y,
                        #                        'r': self.player.playership.r}))

                    elif event.key == pygame.K_m:
                        self.player.playership.mass += 1
                        maxspeed = math.log((0.001 * self.player.playership.mass
                                             ** 1.08)
                                / self.player.playership.thrust, 0.85)
                        print(self.player.playership.mass,
                              self.player.playership.thrust, maxspeed)

                    elif event.key == pygame.K_n:
                        self.player.playership.mass -= 1
                        maxspeed = math.log((0.001 * self.player.playership.mass
                                             ** 1.08)
                                / self.player.playership.thrust, 0.85)
                        print(self.player.playership.mass,
                              self.player.playership.thrust, maxspeed)

                    elif event.key == pygame.K_k:
                        self.player.playership.thrust += 1
                        maxspeed = math.log((0.001 * self.player.playership.mass
                                             ** 1.08)
                                / self.player.playership.thrust, 0.85)
                        print(self.player.playership.mass,
                              self.player.playership.thrust, maxspeed)

                    elif event.key == pygame.K_j:
                        self.player.playership.thrust -= 1
                        maxspeed = math.log((0.001 * self.player.playership.mass
                                             ** 1.08)
                                / self.player.playership.thrust, 0.85)
                        print(self.player.playership.mass,
                              self.player.playership.thrust, maxspeed)

            #----------------------------------------
            #--------------KEY-PRESSED---------------
            #------------------CHAT------------------

                else:
                    if event.key == pygame.K_RETURN:
                        if self.ggci.chat.inputstring is not "":
                            self.ggci.chat.addLine(self.ggci.chat.inputstring)
                            self.ggci.chat.inputstring = ""
                        self.ggci.chat.input = False

                    elif event.key == pygame.K_BACKSPACE:
                        self.ggci.chat.inputstring = self.ggci.chat.inputstring[:-1]

                    elif event.key == pygame.K_ESCAPE:
                        self.ggci.chat.inputstring = ""
                        self.ggci.chat.input = False

                    elif len(self.ggci.chat.inputstring) < 30:

                        self.ggci.chat.inputstring += event.unicode

            #----------------------------------------
            #--------------KEY-RELEASED--------------
            #----------------------------------------

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    self.uevents.w = False

                elif event.key == pygame.K_a:
                    self.uevents.a = False

                elif event.key == pygame.K_d:
                    self.uevents.d = False

            #----------------------------------------
            #---------------NETWORKING---------------
            #----------------------------------------

            elif event.type == pygame.USEREVENT:

                data = event.dict
                if data['type'] == 'fullscreen':

                    self.render.screen = pygame.display.set_mode(self.ggci.ggdata.screensize,
                                              pygame.DOUBLEBUF |
                                              pygame.OPENGL | pygame.FULLSCREEN,
                                              24)
                    self.render.reinit()
                    self.ggci.wm.optionswindow.buttons[0].text = "Windowed"

                if data['type'] == 'windowed':

                    self.render.screen = pygame.display.set_mode(self.ggci.ggdata.screensize,
                                              pygame.DOUBLEBUF |
                                              pygame.OPENGL,
                                              24)
                    self.render.reinit()
                    self.ggci.wm.optionswindow.buttons[0].text = "Fullscreen"

                if data['type'] == 'QUIT':

                    self.running = False

                if data['type'] == 'newspaceobject':

                    spaceship = SpaceShip({'soid': data['soid'], 'x':  0, 'y': 0,
                                           'engine': {'type': "Electromotor", 'thrust': 100, 'mass': 100}}, self.ggci)
                    spaceship.r = 0
                    self.ggci.objectlist.addObject(spaceship)

                if data['type'] == 'removespaceobject':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid']:

                            self.ggci.objectlist.removeObject(objects)

                if data['type'] == 'spaceobjectmoved':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid']:

                            objects.move(data['target'])

                            #objects.nextx = data['x']
                            #objects.nexty = data['y']
                            #objects.nextr = data['r']

                            #if data['x'] > objects.x + 1 or data['x'] < objects.x - 1:
                            #objects.x = data['x']
                            #if data['y'] > objects.y + 1 or data['y'] < objects.y - 1:
                            #objects.y = data['y']
                            #objects.scale_x = data['scale_x']
                            #objects.scale_y = data['scale_y']
                            #objects.speed = data['speed']
                            #objects.angle = data['r']
                            #objects.target = (data['x'], data['y'])

                if data['type'] == 'sendchatmessage':

                    self.ggci.chat.chat.append(data['message'])

                if data['type'] == 'playershot':

                    for objects in self.ggci.objectlist.objectlist:

                        if objects.id == data['soid'] and objects.type == "ss":
                            objects.weapon.shoot(data)


            #----------------------------------------
            #-----------MOTION-CALCULATION-----------
            #----------------------------------------

            if self.uevents.lmsbtn == True:

                if event.type == pygame.MOUSEMOTION:

                    if self.uevents.clickedwindow is not None:

                        self.uevents.clickedwindow.posx += event.rel[0]
                        self.uevents.clickedwindow.posy += event.rel[1]

                    else:

                        if self.uevents.lock == True:

                            self.uevents.lock = False

                        self.player.x += ((event.rel[0] / 100)
                                          + ((self.player.z / 10)
                                             * (event.rel[0] / 100)))
                        self.player.y -= ((event.rel[1] / 100)
                                          + ((self.player.z / 10)
                                             * (event.rel[1] / 100)))

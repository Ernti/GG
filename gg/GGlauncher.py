'''
Created on 11.12.2013

@author: deLordKazz
'''
import pygame
import sys
import os
from gg.GGtextinput import TextInput

pygame.init()

class GGlauncher():

    launcherimgpath = os.path.join(".", "gg", "data", "gfx", "GGLauncher.png")
    
    def __init__(self):
        
        #Entire Screen
        self.sizeX = 500
        self.sizeY = 600
        self.launcherScreen = pygame.display.set_mode((self.sizeX, self.sizeY), pygame.NOFRAME)
        pygame.display.set_caption("GGLauncher")
        
        #Images to render
        self.launcherimg = pygame.image.load(self.launcherimgpath).convert()
           
        #Login Variables
        self.canTypeLoginName = False
        self.canTypePassword = False
        self.loginName = ""
        self.password = ""
        self.passStars = ""
        self.myFont = pygame.font.SysFont("monospace", 20)
        self.countLoginLetters = 0
        self.countPassLetters = 0
        self.shiftIsPressed = False
        self.backspaceIsPressed = False
        self.keyHolder = ""
        self.passHolder = ""
        self.textinput = TextInput()
        
        
    def launcherLoop(self):
        launcherUp = True

        self.background = pygame.Surface((self.sizeX, self.sizeY))
        self.background = self.background.convert()

        clock = pygame.time.Clock()

        while launcherUp == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]

                    print(x, end=", ")
                    print(y)
                         
                    #Usage of Login and Exit Buttons
                    if (x > 386) & (x < 477) & (y > 416) & (y < 474):
                        launcherUp = False
                        return {'username': self.loginName, 'password': 'iminspace'}

                    if (x > 386) & (x < 477) & (y > 496) & (y < 554):
                        launcherUp = False
                        sys.exit()
                    
                    # Whether Password and Username can be entered or not    
                    if (x > 43) & (x < 271) & (y > 416) & (y < 455):
                        self.canTypeLoginName = True
                    
                    if (x < 43) | (x > 271) | (y < 416) | (y > 455):
                        self.canTypeLoginName = False
                        
                    if (x > 43) & (x < 271) & (y > 476) & (y < 516):
                        self.canTypePassword = True
                        
                    if (x < 43) | (x > 271) | (y < 476) | (y > 516):
                        self.canTypePassword = False
                
                
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LSHIFT) | (event.key == pygame.K_RSHIFT):
                        self.shiftIsPressed = True
                        
                    if (event.key == pygame.K_BACKSPACE):
                        self.backspaceIsPressed = True
                        
                if (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_LSHIFT) | (event.key == pygame.K_RSHIFT):
                        self.shiftIsPressed = False
                        
                    if (event.key == pygame.K_BACKSPACE):
                        self.backspaceIsPressed = False
                    
                #Username-Input        
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters <=15):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (self.textinput.isLetter(event.key) == True):
                        self.keyHolder = pygame.key.name(event.key)
                        if (self.shiftIsPressed == True):
                            self.keyHolder = self.keyHolder.capitalize()
                        self.loginName += self.keyHolder
                        print(self.loginName)
                        self.countLoginLetters += 1
                    elif (self.textinput.isDigit(event.key) == True):
                       # if (self.shiftIsPressed == True):
                       #     special = self.textinput.isSpecial(event.key)
                       #     self.keyholder = pygame.key.name(special)
                       # else:
                        self.keyHolder = pygame.key.name(event.key)
                        self.loginName += self.keyHolder
                        print(self.loginName)
                        self.countLoginLetters += 1
                
                #Password-Input        
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters <= 15):
        
                    #Numbers from 0-9 & Letters from a-z
                    if (self.textinput.isLetter(event.key) == True):
                        self.passHolder = pygame.key.name(event.key)
                        if (self.shiftIsPressed == True):
                            self.passHolder = self.passHolder.capitalize()
                        self.password += self.passHolder
                        self.passStars = (self.countPassLetters+1)*"*"
                        print(self.password)
                        self.countPassLetters += 1
                    elif (self.textinput.isDigit(event.key) == True):
                        self.password += pygame.key.name(event.key)
                        self.passStars = (self.countPassLetters+1)*"*"
                        print(self.password)
                        self.countPassLetters += 1
            
            
            
            #Username-Deletion    
            if (self.canTypeLoginName == True) & (self.countLoginLetters > 0) & (self.backspaceIsPressed == True):
                    self.loginName = self.loginName[:-1]
                    print(self.loginName)
                    self.countLoginLetters -= 1    
                
            #Password-Deletion      
            if (self.canTypePassword == True) & (self.countPassLetters > 0) & (self.backspaceIsPressed == True):
                    self.password = self.password[:-1]
                    print(self.password)
                    self.passStars = (self.countPassLetters-1)*"*"
                    self.countPassLetters -= 1            
                    
                    
                    

            self.printLoginTitleFont = self.myFont.render("Username:", 1, (0,0,0))
            self.printPassTitleFont = self.myFont.render("Password:", 1, (0,0,0))
            self.printLoginFont = self.myFont.render(self.loginName, 1, (0,0,0))
            self.printPassFont = self.myFont.render(self.passStars, 1, (0,0,0))
            
            self.background.fill((200, 200, 200))
            self.background.blit(self.launcherimg,(0,0))
            
            #self.background.blit(self.printLoginTitleFont,(25,434))
            #self.background.blit(self.printPassTitleFont,(25,484))
            self.background.blit(self.printLoginFont,(45,426))
            self.background.blit(self.printPassFont,(45,486))

            self.launcherScreen.blit(self.background, (0, 0))
            pygame.display.flip()

            clock.tick(20)
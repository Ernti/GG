'''
Created on 11.12.2013

@author: deLordKazz
'''
import pygame
import sys
import os

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
        
    def isLetter(self,character):
        if (character == pygame.K_a) | (character == pygame.K_b) \
        | (character == pygame.K_c) | (character == pygame.K_d) | (character == pygame.K_e) \
        | (character == pygame.K_f) | (character == pygame.K_g) | (character == pygame.K_h) \
        | (character == pygame.K_i) | (character == pygame.K_j) | (character == pygame.K_k) \
        | (character == pygame.K_l) | (character == pygame.K_m) | (character == pygame.K_n) \
        | (character == pygame.K_o) | (character == pygame.K_p) | (character == pygame.K_q) \
        | (character == pygame.K_r) | (character == pygame.K_s) | (character == pygame.K_t) \
        | (character == pygame.K_u) | (character == pygame.K_v) | (character == pygame.K_w) \
        | (character == pygame.K_x) | (character == pygame.K_y) | (character == pygame.K_z): 
            return True
        else:
            return False
        
    def isDigit(self,character):
        if (character == pygame.K_0) | (character == pygame.K_1) | (character == pygame.K_2) \
        | (character == pygame.K_3) | (character == pygame.K_4) | (character == pygame.K_5) \
        | (character == pygame.K_6) | (character == pygame.K_7) | (character == pygame.K_8) \
        | (character == pygame.K_9):
            return True
        else:
            return False
        
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
                    
                #Username-Entering        
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters <=15):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (self.isLetter(event.key) == True):
                        self.keyHolder = pygame.key.name(event.key)
                        if (self.shiftIsPressed == True):
                            self.keyHolder = self.keyHolder.capitalize()
                        self.loginName += self.keyHolder
                        print(self.loginName)
                        self.countLoginLetters += 1
                    elif (self.isDigit(event.key) == True):
                        keyHolder = pygame.key.name(event.key)
                        self.loginName += keyHolder
                        print(self.loginName)
                        self.countLoginLetters += 1
                
                #Password-Entering        
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters <= 15):
        
                    #Numbers from 0-9 & Letters from a-z
                    if (self.isLetter(event.key) == True):
                        self.passHolder = pygame.key.name(event.key)
                        if (self.shiftIsPressed == True):
                            self.passHolder = self.passHolder.capitalize()
                        self.password += self.passHolder
                        self.passStars = (self.countPassLetters+1)*"*"
                        print(self.password)
                        self.countPassLetters += 1
                    elif (self.isDigit(event.key) == True):
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
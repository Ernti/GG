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
                        
                if (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_LSHIFT) | (event.key == pygame.K_RSHIFT):
                        self.shiftIsPressed = False
                
                #Username-Entering        
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters <=15):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (event.key == pygame.K_0) | (event.key == pygame.K_1) | (event.key == pygame.K_2) \
                    | (event.key == pygame.K_3) | (event.key == pygame.K_4) | (event.key == pygame.K_5) \
                    | (event.key == pygame.K_6) | (event.key == pygame.K_7) | (event.key == pygame.K_8) \
                    | (event.key == pygame.K_9) | (event.key == pygame.K_a) | (event.key == pygame.K_b) \
                    | (event.key == pygame.K_c) | (event.key == pygame.K_d) | (event.key == pygame.K_e) \
                    | (event.key == pygame.K_f) | (event.key == pygame.K_g) | (event.key == pygame.K_h) \
                    | (event.key == pygame.K_i) | (event.key == pygame.K_j) | (event.key == pygame.K_k) \
                    | (event.key == pygame.K_l) | (event.key == pygame.K_m) | (event.key == pygame.K_n) \
                    | (event.key == pygame.K_o) | (event.key == pygame.K_p) | (event.key == pygame.K_q) \
                    | (event.key == pygame.K_r) | (event.key == pygame.K_s) | (event.key == pygame.K_t) \
                    | (event.key == pygame.K_u) | (event.key == pygame.K_v) | (event.key == pygame.K_w) \
                    | (event.key == pygame.K_x) | (event.key == pygame.K_y) | (event.key == pygame.K_z):
                        keyHolder = pygame.key.name(event.key)
                        self.loginName += keyHolder
                        print(self.loginName)
                        self.countLoginLetters += 1
                
                #Username-Deletion    
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters > 0):
                    if (event.key == pygame.K_BACKSPACE):
                        self.loginName = self.loginName[:-1]
                        print(self.loginName)
                        self.countLoginLetters -= 1
                
                #Password-Entering        
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters <= 15):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (event.key == pygame.K_0) | (event.key == pygame.K_1) | (event.key == pygame.K_2) \
                    | (event.key == pygame.K_3) | (event.key == pygame.K_4) | (event.key == pygame.K_5) \
                    | (event.key == pygame.K_6) | (event.key == pygame.K_7) | (event.key == pygame.K_8) \
                    | (event.key == pygame.K_9) | (event.key == pygame.K_a) | (event.key == pygame.K_b) \
                    | (event.key == pygame.K_c) | (event.key == pygame.K_d) | (event.key == pygame.K_e) \
                    | (event.key == pygame.K_f) | (event.key == pygame.K_g) | (event.key == pygame.K_h) \
                    | (event.key == pygame.K_i) | (event.key == pygame.K_j) | (event.key == pygame.K_k) \
                    | (event.key == pygame.K_l) | (event.key == pygame.K_m) | (event.key == pygame.K_n) \
                    | (event.key == pygame.K_o) | (event.key == pygame.K_p) | (event.key == pygame.K_q) \
                    | (event.key == pygame.K_r) | (event.key == pygame.K_s) | (event.key == pygame.K_t) \
                    | (event.key == pygame.K_u) | (event.key == pygame.K_v) | (event.key == pygame.K_w) \
                    | (event.key == pygame.K_x) | (event.key == pygame.K_y) | (event.key == pygame.K_z):
                        self.password += pygame.key.name(event.key)
                        print(self.password)
                        self.passStars = (self.countPassLetters+1)*"*"
                        self.countPassLetters += 1
                
                #Password-Deletion      
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters > 0):
                    if (event.key == pygame.K_BACKSPACE):
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
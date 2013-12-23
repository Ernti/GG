'''
Created on 11.12.2013

@author: deLordKazz
'''
import pygame
import sys
import os

pygame.init()

class GGlauncher():

    lbimgpath = os.path.join(".", "gg", "data", "gfx", "LoginButton.png")
    ebimgpath = os.path.join(".", "gg", "data", "gfx", "ExitButton.png")

    def __init__(self):
        
        #Entire Screen
        self.launcherScreen = pygame.display.set_mode((300, 500), pygame.NOFRAME)
        pygame.display.set_caption("GGLauncher")
        
        #Images to render
        self.lbimg = pygame.image.load(self.lbimgpath).convert()
        self.ebimg = pygame.image.load(self.ebimgpath).convert()
        
        #Login Variables
        self.canTypeLoginName = False
        self.canTypePassword = False
        self.loginName = ""
        self.password = ""
        self.passStars = ""
        self.myFont1 = pygame.font.SysFont("monospace", 15)
        self.myFont2 = pygame.font.SysFont("monospace", 15)
        self.countLoginLetters = 0
        self.countPassLetters = 0
        

    def launcherLoop(self):
        launcherUp = True

        self.background = pygame.Surface((300, 500))
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

                    if (x > 200) & (x < 275) & (y > 350) & (y < 400):
                        launcherUp = False

                    if (x > 200) & (x < 275) & (y > 410) & (y < 460):
                        launcherUp = False
                        sys.exit()
                        
                    if (x > 25) & (x < 175) & (y > 350) & (y < 375):
                        self.canTypeLoginName = True
                    
                    if (x < 25) | (x > 175) | (y < 350) | (y > 375):
                        self.canTypeLoginName = False
                        
                    if (x > 25) & (x < 175) & (y > 385) & (y < 410):
                        self.canTypePassword = True
                        
                    if (x < 25) | (x > 175) | (y < 385) | (y > 410):
                        self.canTypePassword = False
                        
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters <=7):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (event.key == pygame.K_0) | (event.key == pygame.K_1) | (event.key == pygame.K_2) \
                    | (event.key == pygame.K_3) | (event.key == pygame.K_4) | (event.key == pygame.K_5) \
                    | (event.key == pygame.K_6) | (event.key == pygame.K_7) | (event.key == pygame.K_8) \
                    | (event.key == pygame.K_9) | (event.key == pygame.K_a) | (event.key == pygame.K_b) \
                    | (event.key == pygame.K_c) | (event.key == pygame.K_d) | (event.key == pygame.K_e) \
                    | (event.key == pygame.K_f) | (event.key == pygame.K_g) | (event.key == pygame.K_h) \
                    | (event.key == pygame.K_i) | (event.key == pygame.K_j) | (event.key == pygame.K_k) \
                    | (event.key == pygame.K_l) | (event.key == pygame.K_m) | (event.key == pygame.K_n) \
                    | (event.key == pygame.K_o) | (event.key == pygame.K_p) | (event.key == pygame.K_o) \
                    | (event.key == pygame.K_r) | (event.key == pygame.K_s) | (event.key == pygame.K_t) \
                    | (event.key == pygame.K_u) | (event.key == pygame.K_v) | (event.key == pygame.K_w) \
                    | (event.key == pygame.K_x) | (event.key == pygame.K_y) | (event.key == pygame.K_z):
                        self.loginName += pygame.key.name(event.key)
                        print(self.loginName)
                        self.countLoginLetters += 1
                    
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLoginLetters > 0):
                    if (event.key == pygame.K_BACKSPACE):
                        self.loginName = self.loginName[:-1]
                        print(self.loginName)
                        self.countLoginLetters -= 1
                        
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters <= 7):
                    
                    #Numbers from 0-9 & Letters from a-z
                    if (event.key == pygame.K_0) | (event.key == pygame.K_1) | (event.key == pygame.K_2) \
                    | (event.key == pygame.K_3) | (event.key == pygame.K_4) | (event.key == pygame.K_5) \
                    | (event.key == pygame.K_6) | (event.key == pygame.K_7) | (event.key == pygame.K_8) \
                    | (event.key == pygame.K_9) | (event.key == pygame.K_a) | (event.key == pygame.K_b) \
                    | (event.key == pygame.K_c) | (event.key == pygame.K_d) | (event.key == pygame.K_e) \
                    | (event.key == pygame.K_f) | (event.key == pygame.K_g) | (event.key == pygame.K_h) \
                    | (event.key == pygame.K_i) | (event.key == pygame.K_j) | (event.key == pygame.K_k) \
                    | (event.key == pygame.K_l) | (event.key == pygame.K_m) | (event.key == pygame.K_n) \
                    | (event.key == pygame.K_o) | (event.key == pygame.K_p) | (event.key == pygame.K_o) \
                    | (event.key == pygame.K_r) | (event.key == pygame.K_s) | (event.key == pygame.K_t) \
                    | (event.key == pygame.K_u) | (event.key == pygame.K_v) | (event.key == pygame.K_w) \
                    | (event.key == pygame.K_x) | (event.key == pygame.K_y) | (event.key == pygame.K_z):
                        self.password += pygame.key.name(event.key)
                        print(self.password)
                        self.passStars = (self.countPassLetters+1)*"*"
                        self.countPassLetters += 1
                      
                if (event.type == pygame.KEYDOWN) & (self.canTypePassword == True) & (self.countPassLetters > 0):
                    if (event.key == pygame.K_BACKSPACE):
                        self.password = self.password[:-1]
                        print(self.password)
                        self.passStars = (self.countPassLetters-1)*"*"
                        self.countPassLetters -= 1
                    

            self.printLoginFont = self.myFont1.render(self.loginName, 1, (0,0,0))
            self.printPassFont = self.myFont2.render(self.passStars, 1, (0,0,0))
            
            self.background.fill((0, 0, 0))
            self.background.blit(self.lbimg, (200, 350))
            self.background.blit(self.ebimg, (200, 410))
            
            pygame.draw.rect(self.background, (255,255,255), (25,350,150,25))
            pygame.draw.rect(self.background, (255,255,255), (25,385,150,25))
            
            self.background.blit(self.printLoginFont,(27,355))
            self.background.blit(self.printPassFont,(27,390))

            self.launcherScreen.blit(self.background, (0, 0))
            pygame.display.flip()

            clock.tick(20)
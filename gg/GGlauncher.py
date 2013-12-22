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
        self.loginName = ""
        self.myFont = pygame.font.SysFont("monospace", 15)
        self.countLetters = 0
        

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
                        
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLetters <=7):
                    if (event.key != pygame.K_BACKSPACE):
                        self.loginName += pygame.key.name(event.key)
                        print(self.loginName)
                        self.countLetters += 1
                    
                if (event.type == pygame.KEYDOWN) & (self.canTypeLoginName == True) & (self.countLetters > 0):
                    if (event.key == pygame.K_BACKSPACE):
                        self.loginName = self.loginName[:-1]
                        print(self.loginName)
                        self.countLetters -= 1    

            self.printFont = self.myFont.render(self.loginName, 1, (0,0,0))
            
            self.background.fill((0, 0, 0))
            self.background.blit(self.lbimg, (200, 350))
            self.background.blit(self.ebimg, (200, 410))
            
            pygame.draw.rect(self.background, (255,255,255), (25,350,150,25))
            
            self.background.blit(self.printFont,(27,355))

            self.launcherScreen.blit(self.background, (0, 0))
            pygame.display.flip()

            clock.tick(20)
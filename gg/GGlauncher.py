'''
Created on 11.12.2013

@author: deLordKazz
'''
import pygame
import sys
import os

pygame.init()

class GGlauncher():
    
    tbimgpath = os.path.join(".", "gg", "data", "gfx", "TestButton.png")
    
    def __init__(self):
        self.launcherScreen = pygame.display.set_mode((300,500), pygame.NOFRAME)
        self.launcherScreen = pygame.display.set_caption("GGLauncher")
        
    def launcherLoop(self):
        launcherUp = True
        
        self.background = pygame.Surface((300,500))
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
                    
                    if (x > 200) & (x < 250) & (y > 350) & (y < 400):
                        launcherUp = False
                        
                    if (x > 200) & (x < 250) & (y > 410) & (y < 460):
                        launcherUp = False
                        sys.exit()
                        
            self.background.fill((255,255,255))
                    
            #pygame.image.load(self.tbimgpath).convert()
                    #pygame.draw.rect(self.launcherScreen, (0,0,0), [200, 410, 75, 50])    
            pygame.draw.rect(self.background, (255,0,0), [200, 350, 75, 50])
            
            
            self.launcherScreen.blit(self.background,(0,0))
            pygame.display.flip()
            
            clock.tick(20)
            
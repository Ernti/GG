'''
Created on 11.12.2013

@author: deLordKazz
'''
import pygame
import sys

pygame.init()

class GGlauncher():
    
    launcherScreen = pygame.display.set_mode((0,0))
    
    def __init__(self,launcherScreen):
        launcherScreen = pygame.display.set_mode((300,500), pygame.NOFRAME)
        launcherScreen = pygame.display.set_caption("GGLauncher")
        
    def launcherLoop(self):
        launcherUp = True
        paintButtons = True
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
                        
                if launcherUp == paintButtons:
                    self.launcherScreen.fill((255,255,255))
                    
                    pygame.draw.rect(self.launcherScreen, (0,0,0), [200, 410, 75, 50])    
                    pygame.draw.rect(self.launcherScreen, (0,0,0), [200, 350, 75, 50])
            
                    pygame.display.flip()
            
                    clock.tick(20)
            
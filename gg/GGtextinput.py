'''
Created on 02.03.2014

@author: deLordKazz
'''

import pygame

pygame.init()

class GGtextinput ():
    
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
        
    #def isSpecial(self,character):
    #    if (character == pygame.K_0):
    #        return pygame.K_EQUALS
    #    else:
    #        return False
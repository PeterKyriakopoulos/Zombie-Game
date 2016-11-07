# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:48:22 2016

@author: PET3RtheGreat
"""

import pygame

def text_to_screen(screen, text, x, y, size = 12, color = (255, 255, 255), font_type = 'C:/Windows/Fonts/AGENCYR.ttf'):
    
    try:
        
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    
    except Exception:
        raise
#!/usr/bin/env python

import pygame
from pygame import Rect, Surface
from pygame.locals import *

def draw_player(surf,pos):
    x,y = pos
    
    pygame.draw.rect(surf,(0,0,255),(x,y,40,5))
    pygame.draw.rect(surf,(0,0,255),(x+5,y-5,30,5))
    pygame.draw.rect(surf,(0,0,255),(x+10,y-10,20,5))
    pygame.draw.rect(surf,(0,0,255),(x+15,y-15,10,5))
    
def draw_enemy(surf,pos):
    x,y = pos
    
    pygame.draw.circle(surf,(255,0,0),(x,y),10)
    pygame.draw.rect(surf,(255,0,0),(x-15,y-3,30,6))
    pygame.draw.rect(surf,(255,0,0),(x-3,y-3,6,15))

def draw_laser(surf,pos,color):
    pass
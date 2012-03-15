#!/usr/bin.env python

import pygame
from pygame import Rect,Surface
from pygame.locals import *
from pygame import Rect,Surface

import explosionshoot
from explosionshoot import Explosion, Explodes

import graphicshoot
from graphicshoot import draw_player


class PlayerExplosion(Explosion):
    def rand_color(self):
        r = randrange(256)
        return 255, r, 0

class Player(object):
    width = 40
    height = 20
        
    explosion_type = PlayerExplosion
    explosion_radius = 28
    
    def __init__(self,surf,x,y):
        self.x = x
        self.y = y
        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image(surf)
        
    def draw_image(self,surf):
        draw_player(surf, (self.x,self.y))
    
    def update(self, dir):
        if dir == "l":
            self.x -= 3
        elif dir == "r":
            self.x += 3

    def alive(self):
        pass

    def kill(self):
        pass
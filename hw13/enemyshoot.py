#!/usr/bin.env python

import random
from random import randrange

import pygame
from pygame import Rect,Surface
from pygame.locals import *
from pygame.sprite import Group,Sprite 

import shipshoot
from shipshoot import Ship,ShipSpawner

import explosionshoot
from explosionshoot import Explosion, Explodes

import graphicshoot
from graphicshoot import draw_enemy

import utils
from utils import randint_neg

class EnemyGroup(Group):
    def __init__(self):
        Group.__init__(self)
    
    def add(self, *sprites):
        for sprite in sprites:
            Group.add(self, sprite)

class EnemyExplosion(Explosion):
    def rand_color(self):
        r = randrange(256)
        return 255, r, 0

class Enemy(object):
    width = 30
    height = 20
    explosion_type = EnemyExplosion
    explosion_radius = 18
    
    def __init__(self,surf,x,y,vx,vy,color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.bounds = surf.get_rect()
        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image(surf)
    
    def draw_image(self,surf):
        self.surf = surf
        draw_enemy(self.surf,(self.x,self.y))
    
    def update(self, dt):
        vx = self.vx
        vy = self.vy
        
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.x += dx
        self.y += dy
        
        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else:
                vx = -vx
                vy = self.vy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += -2 * dx
                    
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += -2 * dy

    
    def alive(self):
        pass
    
    def kill(self):
        pass

class EnemySpawner(object):
    
    def __init__(self, surf,duration, group, bounds):
        self.surf = surf
        self.group = group
        self.bounds = bounds
        self.duration = duration
        self.time = duration
    
    def spawn(self):
        x = randrange(self.bounds.width - Enemy.width) + self.bounds.left
        y = randrange(self.bounds.height - Enemy.height) + self.bounds.top
        vx, vy = self.rand_vel()
        color = self.rand_color()
        
        ship = Enemy(self.surf,x, y, vx, vy, color)
        self.group.add(ship)
    
    def update(self, dt):
        self.time += dt
        if self.time >= self.duration:
            self.time = 0
            self.spawn()

    def rand_vel(self):
        vx = randint_neg(100, 250)
        vy = randint_neg(100, 250)
        return vx, vy
    
    def rand_color(self):
        r = randrange(128,256)
        return r,0,0
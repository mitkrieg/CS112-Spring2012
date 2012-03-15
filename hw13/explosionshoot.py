#!/usr/bin/env python

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

class ExplosionGroup(Group):
    def draw(self, surf):
        for xplo in self:
            if xplo.radius > 0:
                xplo.draw(surf)

class Explosion(Sprite):
    dradius = 60
    duration = 150
    group = ExplosionGroup()
    
    def __init__(self, pos, radius):
        Sprite.__init__(self)
        self.pos = pos
        self.radius = radius
    
    def update(self, dt):
        if self.duration > 0:
            self.duration -= dt
        elif self.radius > 0:
            self.radius -= self.dradius * (dt / 1000.0)
        else:
            self.kill()
    
    def rand_color(self):
        return randrange(120,256), 255, randrange(120,256)
    
    def draw(self, surf):
        pygame.draw.circle(surf, self.rand_color(), self.pos, int(self.radius))




class Explodes(Sprite):
    explosion_type = Explosion
    explosion_radius = 60
    
    def kill(self):
        xplo = self.explosion_type(self.rect.center, self.explosion_radius)
        Explosion.group.add(xplo)
        Sprite.kill(self)


def collide_xplo_ship(xplo, ship):
    return collide_rect_circle(ship.rect, xplo.pos, xplo.radius)
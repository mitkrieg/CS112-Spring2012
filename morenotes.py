#!/usr/bin/env python

import pygame
from pygame.locals import *

##Settings
BACKGROUND = 80,80,80
SCREEN_SIZE = 800,600
RECT_SIZE = 120,80
RED = 255,0,0
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


bounds = screen.get_rect()
rects = [pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((680,0), RECT_SIZE),
         pygame.Rect((680,500), RECT_SIZE),
         pygame.Rect((0,500), RECT_SIZE)]

rects[0].center = bounds.center
rects[1].topleft = bounds.topleft
rects[2].topright = bounds.topright
rects[3].bottomleft = bounds.bottomleft
rects[4].bottomright = bounds.bottomright


clock = pygame.time.Clock()
done = False
grabbed = False

while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect
        elif evt.type == MOUSEBUTTONUP:
            grabbed = None
            
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)

    screen.fill(BACKGROUND)
    for rect in rects:
        color = RED
        if grabbed == True:
            color = (255,255,255)
    for rect in rects:
        pygame.draw.rect(screen,(color),rect)
        pygame.draw.rect(screen,(0,0,0),rect,5)

    pygame.display.flip()
    clock.tick(FPS)
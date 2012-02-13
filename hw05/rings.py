#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################
pi=3.1415926

pygame.draw.arc(screen, BLUE, (10,20,200,200),-1.135,4.8, THICKNESS)
#pygame.draw.cricle(screen, BLUE,(110,120),100, THICKNESS)
pygame.draw.arc(screen, YELLOW,(120,120,200,200),pi/10,pi/2+.09, THICKNESS)
pygame.draw.arc(screen, YELLOW,(120,120,200,200),pi/2+.45,pi*2-.06, THICKNESS)
#pygame.draw.circle(screen, YELLOW, (220,220), 100, THICKNESS)
pygame.draw.arc(screen,BLACK,(230,20,200,200),-pi/2+.4,pi,THICKNESS)
pygame.draw.arc(screen,BLACK,(230,20,200,200),pi+.35,3*pi/2+.1, THICKNESS)
#pygame.draw.circle(screen, BLACK, (330,120), 100, THICKNESS)
pygame.draw.arc(screen, GREEN,(340,120,200,200),pi/10,pi/2+.09, THICKNESS)
pygame.draw.arc(screen, GREEN,(340,120,200,200),pi/2+.45,pi*2-.06, THICKNESS)
pygame.draw.arc(screen, RED,(450,20,200,200),-pi+.4,pi, THICKNESS)
#pygame.draw.circle(screen, RED, (550,120), 100, THICKNESS)
#pygame.draw.circle(screen, GREEN, (440,220), 100, THICKNESS)

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"

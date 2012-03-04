#!/usr/bin/env python
"""
Creates a game of minespeeper
"""
import pygame
from pygame.locals import *

#Conditions
SCREEN_SIZE = SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
SQUARE_DIMENSIONS = 50,50
BLACK = 0,0,0
WHITE = 255,255,255
GREY = 100,100,100
BLUE = 0, 255, 0
RED = 255 ,0,0
GREEN = 0,0,255
FPS = 30
color = WHITE

#Initiate Screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Minesweeper")
screen.fill(GREY)
squares = []

for i in range(10):
    row = []
    for k in range(10):
        row.append(pygame.Rect((i*50,k*50),SQUARE_DIMENSIONS))
    squares.append(row)

for i, row in enumerate(squares):
    for j, val in enumerate(row):
        pygame.draw.rect(screen,color,squares[i][j])
        pygame.draw.rect(screen,BLACK,squares[i][j],2)

        

#start clock
clock = pygame.time.Clock()
done = False

#Game loop
while not done:
    event = pygame.event.poll()

    #Input and Events
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == MOUSEBUTTONDOWN:
        for square in squares:
            if square.collidepoint(pygame.mouse.get_pos()):
                clicked = square 
    elif event.type == MOUSEBUTTONUP:
        clicked = None

    #Update

    #Draw

    #Refresh
    pygame.display.flip()
    clock.tick(FPS)

print "End"
#!/usr/bin/env python
"""tictactoe.py

A Simple tic tac toe game
"""

# Implement a version of tic tac toe
import pygame
from pygame.locals import *

#COlORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

## MAIN
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#BOARD
pygame.draw.rect(screen, BLACK, (175,50,20,500))
pygame.draw.rect(screen, BLACK, (375,50,20,500))
pygame.draw.rect(screen, BLACK, (50,175,500,20))
pygame.draw.rect(screen, BLACK, (50,375,500,20))

#conditions
player = "o"
square = [True for squ in range(9)]
used = 0

## Loop
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
        
    x,y=pygame.mouse.get_pos()

#   This is a super long if/elif block of code, proabaly should have made a method, but I don't know how to do that in python yet.....

    if x in range (0,175) and y in range (0,175) and event.type == MOUSEBUTTONDOWN and square[0] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (100,100),50, 10)
            player = "x"
            square[0]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (50,50),(155,155), 20)
            pygame.draw.line(screen, RED, (155,50),(50,155),20)
            player = "o"
            square[0]="x"
            used += 1
    elif x in range (195,375) and y in range (0,175) and event.type == MOUSEBUTTONDOWN and square[1] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (275,100),50, 10)
            player = "x"
            square[1]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (210,50),(355,155), 20)
            pygame.draw.line(screen, RED, (210,155),(355,50), 20)
            player = "o"
            square[1]="x"
            used += 1
    elif x in range (395,600) and y in range (0,175) and event.type == MOUSEBUTTONDOWN and square[2] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (475,100),50, 10)
            player = "x"
            square[2]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (410,50),(550,155), 20)
            pygame.draw.line(screen, RED, (410,155),(550,50), 20)
            player = "o"
            square[2]="x"
            used += 1
    elif x in range (0,175) and y in range (195,375) and event.type == MOUSEBUTTONDOWN and square[3] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (100,275),50, 10)
            player = "x"
            square[3]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (50,210),(155,355), 20)
            pygame.draw.line(screen, RED, (155,210),(50,355), 20)
            player = "o"
            square[3]="x"
            used += 1
    elif x in range (195,375) and y in range (195,375) and event.type == MOUSEBUTTONDOWN and square[4] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (275,275),50, 10)
            player = "x"
            square[4]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (210,210),(355,355), 20)
            pygame.draw.line(screen, RED, (355,210),(210,355), 20)
            player = "o"
            square[4]="x"
            used += 1
    elif x in range (395,600) and y in range (195,375) and event.type == MOUSEBUTTONDOWN and square[5] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (475,275),50, 10)
            player = "x"
            square[5]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (410,210),(550,355), 20)
            pygame.draw.line(screen, RED, (410,355),(550,210), 20)
            player = "o"
            square[5]="x"
            used += 1
    elif x in range (0,175) and y in range (395,600) and event.type == MOUSEBUTTONDOWN and square[6] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (100,475),50, 10)
            player = "x"
            square[6]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (50,410),(155,550), 20)
            pygame.draw.line(screen, RED, (155,410),(50,550), 20)
            player = "o"
            square[6]="x"
            used += 1
    elif x in range (195,375) and y in range (395,600) and event.type == MOUSEBUTTONDOWN and square[7] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (275,475),50, 10)
            player = "x"
            square[7]="o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (210,410),(355,550), 20)
            pygame.draw.line(screen, RED, (355,410),(210,550), 20)
            player = "o"
            square[7]="x"
            used += 1
    elif x in range (395,600) and y in range (395,600) and event.type == MOUSEBUTTONDOWN and square[8] == True:
        if player == "o":
            pygame.draw.circle(screen, RED, (475,475),50, 10)
            player = "x"
            square[8]= "o"
            used += 1
        else:
            pygame.draw.line(screen, RED, (410,410),(550,550), 20)
            pygame.draw.line(screen, RED, (540,410),(410,550), 20)
            player = "o"
            square[8]= "x"
            used += 1

    #I couldnt figure out how to get pygame.font to work, so the winner is printed to the console rather than the screen. Sorry

    if square[0]==square[1] and square[1]==square[2] and square[0] is not True:
        print square[0], "wins!!\n"
        done = True
    elif square[0]==square[3] and square[3]==square[6] and square[0] is not True:
        print square[0], "wins!!\n"
        done = True
    elif square[0]==square[4] and square[4]==square[8] and square[0] is not True:
        print square[0], "wins!!\n"
        done = True
    elif square[1]==square[4] and square[4]==square[7] and square[1] is not True:
        print square[1], "wins!!\n"
        done = True
    elif square[2]==square[5] and square[5]==square[8] and square[2] is not True:
        print square[2], "wins!!\n"
        done = True
    elif square[2]==square[4] and square[4]==square[6] and square[2] is not True:
        print square[2], "wins!!\n"
        done = True
    elif square[3]==square[4] and square[4]==square[5] and square[3] is not True:
        print square[3], "wins!!\n"
        done = True
    elif square[6]==square[7] and square[7]==square[8] and square[6] is not True:
        print square[6], "wins!!\n"
        done = True
    elif used == 9:
        print "Tie Game."
        done = True
    
    pygame.display.flip()

print "ByeBye\n"

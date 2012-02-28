#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *

#Colors
BLUE= 0, 133, 199
RED= 255, 0, 0
BLACK = 0,0,0
SCREEN_SIZE = SCREEN_WIDTH,SCREEN_HEIGHT = 800,600

#Initiate screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TRON")
screen.fill(BLACK)

#Draw inital player positions
player_1_posx = 100
player_1_posy = 300
player_2_posx = 700
player_2_posy = 300

pygame.draw.circle(screen,RED,(player_1_posx,player_1_posy),3)
pygame.draw.circle(screen,BLUE,(player_2_posx,player_2_posy),3)


#creating lists storing previous positions
player1x = [player_1_posx]
player1y = [player_1_posy]
player2x = [player_2_posx]
player2y = [player_2_posy]

direction1 = "right"
direction2 = "left"

def positioncheck():
    if player_1_posx < 2 or player_2_posx < 2 or player_1_posy < 2 or player_2_posy < 2:
        return True
    elif player_1_posx > 798 or player_2_posx > 798 or player_1_posy > 598 or player_2_posy > 598:
        return True
    for test in range(len(player1x)):
        if player1x[test] == player_1_posx and player1y[test] == player_1_posy:
            return True
    for test in range(len(player1x)):
        if player1x[test] == player_2_posx and player1y[test] == player_2_posy:
            return True
    for test in range(len(player1x)):
        if player2x[test] == player_1_posx and player2y[test] == player_1_posy:
            return True
    for test in range(len(player1x)):
        if player2x[test] == player_2_posx and player2y[test] == player_2_posy:
            return True
                      
 
def quitter():
    if event.type == QUIT:
        return True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return True

clock = pygame.time.Clock()
done = False
begun = False
event = pygame.event.poll()

while not begun:
    event = pygame.event.poll()
    begun = quitter()
    
    if event.type == KEYDOWN and event.key == K_SPACE:
        del player1x[:]
        del player1y[:]
        del player2x[:]
        del player2y[:]
        
        player_1_posx = 100
        player_1_posy = 300
        player_2_posx = 700
        player_2_posy = 300

        screen.fill(BLACK)
        pygame.draw.circle(screen,RED,(player_1_posx,player_1_posy),3)
        pygame.draw.circle(screen,BLUE,(player_2_posx,player_2_posy),3)

    if event.type == KEYDOWN and event.key == K_SPACE:
        direction1 = "right"
        direction2 = "left"
        done = False

    pygame.display.flip()
    clock.tick(30)

    if event.type == KEYDOWN and event.key == K_SPACE:
        while not done:
            event = pygame.event.poll()
            done = quitter()
            
            pygame.key.set_repeat()
            if event.type == KEYDOWN and event.key == K_UP:
                direction1 = "up" 
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_DOWN:
                direction1 = "down"
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_LEFT:
                direction1 = "left"
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                direction1 = "right"
                pygame.key.set_repeat()
            
            
            pygame.key.set_repeat()
            if event.type == KEYDOWN and event.key == K_w:
                direction2 = "up"
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_s:
                direction2 = "down"
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_d:
                direction2 = "right"
                pygame.key.set_repeat()
            elif event.type == KEYDOWN and event.key == K_a:
                direction2 = "left"
                pygame.key.set_repeat()
            
            
            if direction1 == "up":
                player_1_posy -= 2
            elif direction1 == "down":
                player_1_posy += 2
            elif direction1 == "left":
                player_1_posx -= 2
            elif direction1 == "right":
                player_1_posx += 2
            
            if direction2 == "up":
                player_2_posy -= 2
            elif direction2 == "down":
                player_2_posy += 2
            elif direction2 == "left":
                player_2_posx -= 2
            elif direction2 == "right":
                player_2_posx += 2
            
            done = positioncheck()
            
            pygame.draw.circle(screen,RED,(player_1_posx,player_1_posy),3)
            pygame.draw.circle(screen,BLUE,(player_2_posx,player_2_posy),3)
            
            player1x.append(player_1_posx)
            player1y.append(player_1_posy)
            player2x.append(player_2_posx)
            player2y.append(player_2_posy)
            
            pygame.display.flip()
            clock.tick(30)



print "End"
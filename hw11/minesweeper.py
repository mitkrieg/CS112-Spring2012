#!/usr/bin/env python
"""
Creates a game of minespeeper
"""
import pygame
from pygame.locals import *
from random import randrange

#Conditions
SCREEN_SIZE = SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
SQUARE_DIMENSIONS = 50
WIDTH = 10
HEIGHT = 10

BLACK = 0,0,0
HIDDEN = 80,80,80
ACTIVE = 220,220,200
WHITE = 255,255,255
CLEARED = 160,160,160
GREY = 100,100,100
BLUE = 0, 240, 0
RED = 240 ,0,0
GREEN = 0,0,240
PURPLE = 240,0,240
YELLOW = 240,240

FPS = 30
color = WHITE
BOMBS = 10



def calc_counts(x,y,bombs):
    font = pygame.font.Font(None,40)
    count = 0
    for i in bombs:
        a,b = i
        if a+1 == x and b == y:
            count += 1
        if a-1 == x and b == y:
            count += 1
        if a == x and b+1 == y:
            count += 1
        if a == x and b-1 == y:
            count += 1
        if a+1 == x and b+1 == y:
            count += 1
        if a-1 == x and b-1 == y:
            count += 1
        if a+1 == x and b-1 == y:
            count += 1
        if a-1 == x and b+1 == y:
            count += 1
        if a == x and b == y:
            return ""
    if count == 0:
        return str("")
    elif count == 1:
        return str(count)
    elif count == 2:  
        return str(count)
    elif count == 3:
        return str(count)
    else:
        return str(count)

def calc_color(x,y,bombs):
    font = pygame.font.Font(None,40)
    count = 0
    for i in bombs:
        a,b = i
        if a+1 == x and b == y:
            count += 1
        if a-1 == x and b == y:
            count += 1
        if a == x and b+1 == y:
            count += 1
        if a == x and b-1 == y:
            count += 1
        if a+1 == x and b+1 == y:
            count += 1
        if a-1 == x and b-1 == y:
            count += 1
        if a+1 == x and b-1 == y:
            count += 1
        if a-1 == x and b+1 == y:
            count += 1
        if a == x and b == y:
            return BLUE
    if count == 0:
        return BLUE
    elif count == 1:
        return BLUE
    elif count == 2:  
        return RED
    elif count == 3:
        return GREEN
    else:
        return PURPLE



def place_bombs(numbombs):
    placed=[]
    for bomb in range(numbombs):
        x = randrange(WIDTH)
        y = randrange(HEIGHT)
        if [x,y] not in placed:
            placed.append([x,y])
    return placed
        
        


#Game loop
def game(screen):
    clock = pygame.time.Clock()
    done = False
    mouseclick = False
    over = False
    font = pygame.font.Font(None,40)
    bounds = screen.get_rect()
    bombcells = place_bombs(BOMBS)
    
                
    squares = []
                
    for i in range(10):
        row = []
        for k in range(10):
            row.append(pygame.Rect(i*50,k*50,SQUARE_DIMENSIONS,SQUARE_DIMENSIONS))
        squares.append(row)
    
    cleared = []
    clear_square = False
    flagged = []
    flag_square = False

    for i in range(10):
        row = []
        for k in range(10):
            row.append(False)
        cleared.append(row)

    for i in range(10):
        row = []
        for k in range(10):
            row.append(False)
        flagged.append(row)

    while not done:
        #Input and Events
        for evt in pygame.event.get():
            if evt.type == QUIT:
                done = True
            elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                done = True
            elif evt.type == MOUSEBUTTONDOWN and evt.button == 1:
                mouseclick = True
            elif evt.type == MOUSEBUTTONUP and evt.button == 1:
                mouseclick = True
                clear_square = True
            elif evt.type == MOUSEBUTTONDOWN and evt.button == 3:
                mouseclick == True
            elif evt.type == MOUSEBUTTONUP   and evt. button == 3:
                mouseclick == True
                flag_square == True
                


        #Update
        if clear_square:
            x,y = pygame.mouse.get_pos()
            x /= SQUARE_DIMENSIONS
            y /= SQUARE_DIMENSIONS
            cleared[y][x] = True
            clear_square = False
        if flag_square:
            x,y = pygame.mouse.get_pos()
            x /= SQUARE_DIMENSIONS
            y /= SQUARE_DIMENSIONS
            flagged[y][x] = True
            flag_square = False
        

        #Draw
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cell = squares[y][x]

                if cleared[x][y]:
                    color = CLEARED
                    
                elif mouseclick and cell.collidepoint(pygame.mouse.get_pos()):
                    color = ACTIVE
                else:
                    color = HIDDEN

                screen.fill(color,cell.inflate(-2,-2))
                


                if cleared[x][y]:
                    for i in bombcells:
                        j,k = i
                        if x == j and y == k:
                            pygame.draw.circle(screen,RED,(y*50+25,x*50+25),10)                    
                            over = True
                    count = font.render(calc_counts(x,y,bombcells),True,calc_color(x,y,bombcells))
                    location = count.get_rect()
                    location.center = squares[y][x].center
                    screen.blit(count, location)
                elif flagged[x][y]:
                    flg = font.render("F",True,RED)
                    location = flg.get_rect()
                    location.center = squares[y][x].center
                    screen.blit(flg, location)

                            
        if len(cleared) == 90:
            text = font.render("WINNER", True, (0,0,255))
            location = text.get_rect()
            location.center = bounds.center
            screen.blit(text, location)
        elif over:
            text = font.render("GAME OVER", True, (0,255,0))
            location = text.get_rect()
            location.center = bounds.center
            screen.blit(text, location)

        #Refresh
        pygame.display.flip()
        clock.tick(FPS)

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Minesweeper")
    game(screen)

main()

print "End"
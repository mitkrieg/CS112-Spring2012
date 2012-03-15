#!/usr/bin/env python

import pygame
from pygame.locals import *

import graphicshoot
from graphicshoot import draw_player,draw_enemy

import explosionshoot
from explosionshoot import ExplosionGroup,Explosion

import enemyshoot
from enemyshoot import EnemyGroup,Enemy,EnemySpawner

import playershoot
from playershoot import Player

class Application(object):
    title = None
    screen_size = 800, 600
    screen_flags = DOUBLEBUF|HWSURFACE|SRCALPHA
    fps = 30
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size, self.screen_flags)
        if self.title:
            pygame.display.set_caption(self.title)
        
        font = pygame.font.Font(None, 60)
        self._paused_text = font.render("Press Space to Resume", True, (255,255,255), (0,0,0))
        self._paused_text.set_colorkey((0,0,0))
        
        self.paused = False
    
    def pause(self):
        self.paused = True
        self.on_pause()
        self._draw_pause()
    
    def _draw_pause(self):
        overlay = pygame.Surface(self.screen.get_size())
        overlay.set_alpha(200)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0,0))
        
        loc = self._paused_text.get_rect()
        loc.center = self.screen.get_rect().center
        self.screen.blit(self._paused_text, loc)
        pygame.display.flip()
    
    
    def resume(self):
        self.paused = False
        self.on_resume()
    
    def quit(self):
        self.done = True
    
    def step(self):
        self.clock.tick(self.fps)
        
        # pause if screen is hidden
        if not pygame.display.get_active() and not self.paused:
            self.pause()
        
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.quit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if self.paused:
                    self.resume()
                else:
                    self.pause()
            elif event.type == VIDEOEXPOSE:
                print "woo"
            else:
                self.handle_event(event)
        
        # update if not paused
        if not self.paused:
            self.update()
            self.draw(self.screen)
            pygame.display.flip()
                
    
    
    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.on_start()
        while not self.done:
            self.step()
        self.on_quit()       
    
    # update if not paused
    
    
    def handle_event(self,event): pass
    def update(self): pass
    def draw(self, screen): pass
    
    def on_resume(self): pass
    def on_pause(self): pass
    def on_start(self): pass
    def on_quit(self): pass

class Game(Application):
    title = "Shoot Em'"
    screen_size = 800, 600
    moving = False
    
    def __init__(self):
        Application.__init__(self)
        
        self.player = Player(self.screen,300,550)
        self.enemy = Enemy(self.screen,300,150,20,20)
        self.bounds = self.screen.get_rect()
        self.enemyGroup = EnemyGroup()
        self.xplos = ExplosionGroup()
        Explosion.group = self.xplos
        self.direction = None
    
        self.spawners = [EnemySpawner(1000, self.enemyGroup, self.bounds)]
        
            
    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_LEFT:
            self.moving = True
            self.direction = "l"
        elif event.type == KEYUP and event.key == K_LEFT:
            self.moving = False
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            self.moving = True
            self.direction = "r"
        elif event.type == KEYUP and event.key == K_RIGHT:
            self.moving = False

    
    def update(self):
        dt = min(200, self.clock.get_time())
        self.enemy.update(dt)
        if self.moving:
            self.player.update(self.direction)
    
                
        for spawner in self.spawners:
            spawner.update(dt)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        self.player.draw_image(screen)
        self.enemy.draw_image(screen)

if __name__ == "__main__":
    Game().run()
    print "End"


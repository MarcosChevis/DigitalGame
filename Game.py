#Main game structure
import pygame, sys
from pygame.locals import *
from Map import Map

pygame.init()

class Game:

    def __init__(self) -> None:

        pygame.display.set_caption('This Game')

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = (800, 600)

        self.font = pygame.font.SysFont("Impact", 40)
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)

        self.clock.tick(30)

        self.map = Map()
        while True:
            self.Loop()

    def gameLoop(self):
        self.eventLoop()

    def eventLoop():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                print("keydown events")

            if event.type == KEYUP:
                print("keyup events")
    
    def gameTick(self):
        self.tick_time = self.clock.tick()
        self.mouse_pos = pygame.mouse.get_pos()
        self.keys_pressed = pygame.key.get_pressed()

    def gameDraw(self):
        self.screen.fill((0, 0, 0))




#Main game structure
import pygame, sys
from pygame.key import name
from pygame.locals import *
from Background import Background

pygame.init()

class Game:

    def __init__(self):

        pygame.display.set_caption('This Game')

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = (800, 600)

        self.font = pygame.font.SysFont("Impact", 40)
        self.screen = pygame.display.set_mode(self.screen_res, 0, 32)

        self.clock.tick(30)

        self.background = Background()

        self.mode = 0

        while True:
            self.gameLoop()

    def gameLoop(self):
        self.eventLoop()
        self.gameTick()
        self.gameDraw()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                print("keydown events")

            if event.type == KEYUP:
                print("keyup events")

            if event.type == MOUSEBUTTONUP:
                #se tiver na mesma posiçao que o botao 1
                if self.mouse_pos[0] < self.screen_res[0]/2:
                    self.mode = 1

                #se tiver na mesma posiçao que o botao 2
                #if self.mouse_pos[0], dfsja:
                pass

    
    def gameTick(self):
        self.tick_time = self.clock.tick()
        self.mouse_pos = pygame.mouse.get_pos()
        self.keys_pressed = pygame.key.get_pressed()

    def gameDraw(self):
        self.screen.fill((0, 0, 0))
        
        i = 0
        background = self.background.getBackground(self.mode)
        while i < background[0].__len__():
            self.screen.blit(background[0][i], background[1][i])
            i += 1
        
        #blit entidades
    

        pygame.display.update()


if __name__ == "__main__":
    Game()
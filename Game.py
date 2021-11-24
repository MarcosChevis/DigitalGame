#Main game structure
import pygame, sys
from pygame.key import name
from pygame.locals import *
from Background import Background
from Entity import Entity
from Player import Player

pygame.init()

class Game:

    def __init__(self):

        pygame.display.set_caption('This Game')

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = (1000, 750)

        self.font = pygame.font.SysFont("Impact", 40)
        self.screen = pygame.display.set_mode(self.screen_res, 0, 32)

        self.clock.tick(30)

        self.background = Background(self)
        self.entity = Entity(self)
        self.player = Player(self)

        self.mode = 0
        
        self.char = 0
        #["name 100"]
        self.leaderboard = []

        self.playerSprites = pygame.sprite.Group()
        self.playerSprites.add(self.player)

        self.counter = 0
        self.speed = 0

        self.entities = []

        self.score = 0

        self.mustEat = 0

        pygame.mixer.init()
        pygame.mixer.music.load("assets/Music/Music.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()

        while True:
            self.gameLoop()

    def gameLoop(self):
        self.eventLoop()
        self.gameTick()
        self.gameDraw()

    def eventLoop(self):
        if self.mode == 0:
            self.launchLoop()
        elif self.mode == 1:
            self.menuLoop()
        elif self.mode == 2:
            self.charSelect()
        elif self.mode == 3:
            self.leaderboardLoop()
        #game 1
        elif self.mode == 4:
            self.runningGame()
        elif self.mode == 5:
            self.jumpingGame()
        elif self.mode == 6:
            self.eatingGame()
        elif self.mode == 7:
            self.gameOver()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                print("keydown events")

            if event.type == KEYUP:
                print("keyup events")

            if event.type == MOUSEBUTTONUP:
                pass

    
    def gameTick(self):
        self.tick_time = self.clock.tick()
        self.mouse_pos = pygame.mouse.get_pos()
        self.keys_pressed = pygame.key.get_pressed()

    def gameDraw(self):
        self.screen.fill((255, 255, 255))
        
        i = 0
        background = self.background.getBackground(self.mode, self.last_tick)
        while i < background.__len__():
            color = background[i][0]
            rectangle = background[i][1]

            pygame.draw.rect(self.screen, color, rectangle)
            i += 1
        
        #blit entidades
        i = 0
        self.entities = self.entity.getEntities(self.mode, self.last_tick)
        while i < self.entities.__len__():
            
            self.screen.blit(self.entities[i][0], self.entities[i][1])
            i += 1

        if self.mode == 4 or self.mode == 5 or self.mode == 6:
            self.playerSprites.draw(self.screen)
            self.playerSprites.update()
        pygame.display.update()


    def launchLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                self.mode = 1

            if event.type == MOUSEBUTTONDOWN:
                self.mode = 1
        

    def menuLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                if self.mouse_pos[0] > 275 and self.mouse_pos[0] < 700:
                    if self.mouse_pos[1] > 160 and self.mouse_pos[1] <  260:
                        self.mode = 2
                    if self.mouse_pos[1] > 300 and self.mouse_pos[1] <  400:
                        self.mode = 3
                    if self.mouse_pos[1] > 460 and self.mouse_pos[1] <  560:
                        pygame.quit()
                        sys.exit()

    def charSelect(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                if self.mouse_pos[0] > 30 and self.mouse_pos[0] < 200:
                    if self.mouse_pos[1] > 30 and self.mouse_pos[1] < 73:
                        self.mode = 1
                if self.mouse_pos[1] > 200 and self.mouse_pos[1] < 600:
                    if self.mouse_pos[0] > 200 and self.mouse_pos[0] < 348:
                        self.char = 0
                        self.player.stopEating()
                        self.mode = 4
                    if self.mouse_pos[0] > 650 and self.mouse_pos[0] < 800:
                        self.char = 1
                        self.player.stopEating()
                        self.mode = 4

    def leaderboardLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                if self.mouse_pos[0] > 30 and self.mouse_pos[0] < 200:
                    if self.mouse_pos[1] > 30 and self.mouse_pos[1] < 73:
                        self.mode = 1

    def runningGame(self):
        self.counter += 1
        if self.counter >= 600:
            self.counter = 0
            self.mode = 5
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.acceleratePlayer()
                    self.speed += 1
                    self.score += 10

    def jumpingGame(self):
        self.counter += 1
        if self.counter >= 1000:
            self.counter = 0
            self.mustEat = int(self.speed/2)
            self.player.startEating()
            self.speed = 0
            self.mode = 6
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if self.player.rect.topleft[1] >= 440:
                        self.player.jump()
        playerRect = Rect(self.player.rect)
        playerRect.size = (playerRect.size[0]-130, playerRect.size[1]-50)
        obstacleRect = Rect(self.entities[0][1][0], self.entities[0][1][1], 58, 116)
        if obstacleRect.colliderect(playerRect):
            self.score -= 1
            

    def eatingGame(self):
        print(self.mustEat)
        self.counter += 1
        if self.counter >= 600:
            self.counter = 0
            self.score = self.score - abs(self.mustEat*10)
            self.player.stopEating()
            self.leaderboard.append(self.score)
            self.score = 0
            self.mode = 7
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.atual = self.player.atual + 1
                    if self.player.atual >= len(self.player.sprites):
                        self.mustEat -= 1
                        self.player.atual = 0
                    self.player.image = self.player.sprites[int(self.player.atual)]
                    self.player.image = pygame.transform.scale(self.player.image, (74*3, 96*3))
    
    def gameOver(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                if self.mouse_pos[0] > 275 and self.mouse_pos[0] < 700:
                    if self.mouse_pos[1] > 160 and self.mouse_pos[1] <  260:
                        self.mode = 2
                    if self.mouse_pos[1] > 300 and self.mouse_pos[1] <  400:
                        self.mode = 3
                    if self.mouse_pos[1] > 460 and self.mouse_pos[1] <  560:
                        pygame.quit()
                        sys.exit()
                if self.mouse_pos[0] > 30 and self.mouse_pos[0] < 200:
                    if self.mouse_pos[1] > 30 and self.mouse_pos[1] < 73:
                        self.mode = 1


if __name__ == "__main__":
    Game()
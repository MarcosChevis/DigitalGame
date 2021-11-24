import pygame, sys, os, random

class Player(pygame.sprite.Sprite):

    def __init__(self, delegate):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        #self.sprites.append(pygame.image.load("Pedrinho/Correndo/R1.png")) #Parado
        self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R2.png"))
        self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R3.png"))
        self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R4.png"))
        self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R5.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (74*3, 96*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 450

        self.direction = 0
        self.alt = 0

        self.eating = False

        self.delegate = delegate

        self.increment = 0.01

    def update(self):
        if self.eating == False:
            self.atual = self.atual + self.increment
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            #largura = 74 e altura = 96
            self.image = pygame.transform.scale(self.image, (74*3, 96*3))

            if self.direction == 1 and self.alt < 150:
                self.rect.topleft =  100, self.rect.topleft[1]-4
                self.alt += 4
            if self.direction == -1 and self.alt >= 4:
                self.rect.topleft =  100, self.rect.topleft[1]+4
                self.alt -= 4
            
            if self.alt >= 150:
                self.direction = -1

            if self.alt <= 0:
                self.direction = 0
        else:
            pass


    def jump(self):
        self.direction = 1

    def acceleratePlayer(self):
        self.increment += 0.004

    def startEating(self):
        self.sprites = []
        #self.sprites.append(pygame.image.load("Pedrinho/Correndo/R1.png")) #Parado
        if self.delegate.char == 0:
            self.sprites.append(pygame.image.load("assets/Paula/Comendo/meninaCo0.png"))
            self.sprites.append(pygame.image.load("assets/Paula/Comendo/meninaCo1.png"))
            self.sprites.append(pygame.image.load("assets/Paula/Comendo/meninaCo2.png"))

        if self.delegate.char == 1:
            self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo/C1.png"))
            self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo//C2.png"))
            self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo//C3.png"))



        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (74*3, 96*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 450

        self.direction = 0
        self.alt = 0

        self.eating = True
        self.increment = 0.06

    def stopEating(self):
        self.sprites = []
        #self.sprites.append(pygame.image.load("Pedrinho/Correndo/R1.png")) #Parado
        if self.delegate.char == 0:
            self.sprites.append(pygame.image.load("assets/Paula/Correndo/meninaC1.png"))
            self.sprites.append(pygame.image.load("assets/Paula/Correndo/meninaC2.png"))
            self.sprites.append(pygame.image.load("assets/Paula/Correndo/meninaC3.png"))
            self.sprites.append(pygame.image.load("assets/Paula/Correndo/meninaC4.png"))

        if self.delegate.char == 1:
            self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R2.png"))
            self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R3.png"))
            self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R4.png"))
            self.sprites.append(pygame.image.load("assets/Pedrinho/Correndo/R5.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (74*3, 96*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 450

        self.direction = 0
        self.alt = 0

        self.eating = False
        self.increment = 0.01

        
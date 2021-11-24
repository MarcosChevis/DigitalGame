import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sprites Teste")

class Pedrinho(pygame.sprite.Sprite):
    def __init__(self):
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
        self.rect.center = (500, 600)

        self.direction = 0
        self.alt = 0

    def update(self):
        self.atual = self.atual + 0.12
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

    def jump(self):
        self.direction = 1


todas_sprites = pygame.sprite.Group()
pedro = Pedrinho()
todas_sprites.add(pedro)

relogio = pygame.time.Clock()
rectposY = pedro.rect.bottom
rectposX = 640

i = 0
while True:
    relogio.tick(60)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            pedro.jump()

    if rectposX <= 0:
        rectposX = 640
    rectposX -= 4
    obstaculo = Rect(rectposX-10, rectposY - 115, 10, 70)

    pedroRect = Rect(pedro.rect)
    pedroRect.size = (pedroRect.size[0]-130, pedroRect.size[1]-50)
    pedroRect.midtop = pedro.rect.midtop


    pygame.draw.rect(tela, (0,0,0), obstaculo)
    pygame.draw.rect(tela, (70,0,0), pedroRect)

    
    
    if obstaculo.colliderect(pedroRect):
        print("perdeu", i)
        i += 1

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()

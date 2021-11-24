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
        self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo/C1.png"))
        self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo//C2.png"))
        self.sprites.append(pygame.image.load("assets/Pedrinho/Comendo//C3.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (74*3, 96*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

    def update(self):
        pass
        # self.atual = self.atual + 0.12
        # if self.atual >= len(self.sprites):
        #     self.atual = 0
        # self.image = self.sprites[int(self.atual)]
        # #largura = 74 e altura = 96
        # self.image = pygame.transform.scale(self.image, (74*3, 96*3))


todas_sprites = pygame.sprite.Group()
pedro = Pedrinho()
todas_sprites.add(pedro)

relogio = pygame.time.Clock()

i = 0

while True:
    relogio.tick(60)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_e:
                pedro.atual = pedro.atual + 1
                if pedro.atual >= len(pedro.sprites):
                    pedro.atual = 0
                    i += 1
                pedro.image = pedro.sprites[int(pedro.atual)]
                #largura = 74 e altura = 96
                pedro.image = pygame.transform.scale(pedro.image, (74*3, 96*3))
    
        

    print(i)
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()

import pygame, sys, os

class Background:

    def __init__(self):
        self.images = []
        self.positions = []
        self.previousMode = 0

        self.setTitleBackground()

    def getBackground(self, mode):
        if mode != self.previousMode:
            self.images = []
            self.positions = []

            if mode == 0:
                self.setTitleBackground()
                
            elif mode == 1:
                self.images.append(pygame.image.load("assets/branco.png").convert_alpha())
                self.positions.append((0, 0))
        
        self.previousMode = mode
        return [self.images, self.positions]

    def setTitleBackground(self):
        self.images.append(pygame.image.load("assets/branco.png").convert_alpha())
        self.positions.append((0, 0))

        self.images.append(pygame.image.load("assets/TituloTest01.png").convert_alpha())
        size = self.images[1].get_rect().size
        posX = (800/2) - (size[0]/2)
        posY = (600/2) - (size[1]/2)
        self.positions.append((posX, posY))

import pygame, sys, os, random

class Background:

    def __init__(self, delegate):
        self.images = []
        self.previousMode = 0

        self.delegate = delegate

        self.buildings = []

        self.setTitleBackground()

    def getBackground(self, mode, last_tick):
                
        self.images = []

        if mode == 0:
            self.setTitleBackground()
            
        elif mode == 1:
            self.setMenuScreenBackground()
        
        elif mode == 2:
            self.setSelectCharBackground()

        elif mode == 3:
            self.setLeaderboardBackground()

        elif mode == 4 or mode == 5 or mode == 6:
            self.setRunningBakcground()



        return self.images

    def setTitleBackground(self):
        self.images.append(((255, 255, 255), pygame.Rect(0, 0, 1000, 750)))

    def setMenuScreenBackground(self):
        self.images.append(((255, 255, 255), pygame.Rect(0, 0, 1000, 750)))
    
    def setSelectCharBackground(self):
        self.images.append(((255, 255, 255), pygame.Rect(0, 0, 1000, 750)))

    def setLeaderboardBackground(self):
        self.images.append(((255, 255, 255), pygame.Rect(0, 0, 1000, 750)))

    def setRunningBakcground(self):
        self.images.append(((173, 216, 230), pygame.Rect(0, 0, 1000, 750)))
        if self.buildings.__len__() == 0:
            self.buildings.append(pygame.Rect(1000, 400, 100, 1000-400))

        if self.buildings[self.buildings.__len__() - 1].topright[0] <= 1000:
            alt = random.randint(400, 700)
            self.buildings.append(pygame.Rect(1000, alt, 100, 1000-alt))
            
        for b in self.buildings:
            b.topleft = (b.topleft[0] - self.delegate.speed/5, b.topleft[1])
            self.images.append(((0, 0, 0), b))

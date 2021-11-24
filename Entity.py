import pygame, sys, os, random

class Entity:

    def __init__(self, delegate):
        #[(image, pos),(),()]
        self.images = []
        self.previousMode = 0

        pygame.font.init()
        self.myFont = pygame.font.SysFont("arial", 20)

        self.delegate = delegate

        self.obstaclePos = [900, 600]

        

    def getEntities(self, mode, last_tick):
                
        self.images = []

        if mode == 0:
            self.setTitleEntities()
            
        elif mode == 1:
            self.setMenuEntities()

        elif mode == 2:
            self.setSelectCharEntities()

        elif mode == 3:
            self.setLeaderboardEntities()

        elif mode == 4:
            self.setRunningEntities()

        elif mode == 5:
            self.setJumpingEntities()

        elif mode == 6:
            self.setEatingEntities()

        elif mode == 7:
            self.setGameOverEntities()
        
        return self.images

    def setTitleEntities(self):
        image = [pygame.image.load("assets/TitleScreen/TituloTest01.png").convert_alpha(), (0, 0)]
        self.images.append(image)
        return self.images

    def setMenuEntities(self):
        image01 = [pygame.image.load("assets/MenuScreen/ComecarJogo.png").convert_alpha(), (275, 140)]
        image02 = [pygame.image.load("assets/MenuScreen/Leaderboard.png").convert_alpha(), (275, 300)]
        image03 = [pygame.image.load("assets/MenuScreen/Sair.png").convert_alpha(), (275, 460)]
        self.images.append(image01)
        self.images.append(image02)
        self.images.append(image03)
        return self.images

    def setSelectCharEntities(self):
        image01 = [pygame.image.load("assets/Paula/Still/PaulaStill.png").convert_alpha(), (200, 200)]
        image02 = [pygame.image.load("assets/Pedrinho/Still/PedroStill.png").convert_alpha(), (650, 200)]
        image03 = [pygame.image.load("assets/MenuScreen/VoltarMenu.png").convert_alpha(), (30, 30)]
        self.images.append(image01)
        self.images.append(image02)
        self.images.append(image03)
        return self.images

    def setLeaderboardEntities(self):
        image01 = [pygame.image.load("assets/MenuScreen/VoltarMenu.png").convert_alpha(), (30, 30)]
        self.images.append(image01)
        if self.delegate.leaderboard.__len__() == 0:
            image02 = [self.myFont.render("Sem Dados de Leaderboard ainda", False, (0, 0, 0)), (300, 160)]
            self.images.append(image02)

        pos = [300, 160]
        i = 0
        sortedArray = sorted(self.delegate.leaderboard)
        for text in sortedArray:
            if i > 9:
                break
            image02 = [self.myFont.render(str(text), False, (0, 0, 0)), (pos[0], pos[1]+(25*i))]
            self.images.append(image02)
            i += 1

        return self.images

    def setRunningEntities(self):
        image02 = [self.myFont.render("Pontuação: " + str(self.delegate.score), False, (0, 0, 0)), (340, 30)]
        self.images.append(image02)
        return self.images

    def setJumpingEntities(self):
        speed = self.delegate.speed
        gameFrame = self.delegate.counter
        initialPos = [900, 600]
        self.obstaclePos[0] = self.obstaclePos[0] - (speed/5)
        if self.obstaclePos[0] <= 20:
            self.obstaclePos = initialPos
        image01 = [pygame.image.load("assets/JumpingGame/Obstacle.png").convert_alpha(), (self.obstaclePos[0], initialPos[1])]
        self.images.append(image01)
        image03 = [self.myFont.render("Pontuação: " + str(self.delegate.score), False, (0, 0, 0)), (340, 30)]
        self.images.append(image03)
        return self.images

    def setEatingEntities(self):
        image02 = [self.myFont.render("Pontuação: " + str(self.delegate.score), False, (0, 0, 0)), (340, 30)]
        image03 = [self.myFont.render("Deve Comer: " + str(self.delegate.mustEat), False, (0, 0, 0)), (340, 50)]
        self.images.append(image02)
        self.images.append(image03)
        return self.images

    def setGameOverEntities(self):
        image = [self.myFont.render("Sua pontuação foi: " + str(self.delegate.leaderboard[0]), False, (0, 0, 0)), (340, 30)]
        image01 = [pygame.image.load("assets/MenuScreen/JogaerNovamente.png").convert_alpha(), (275, 140)] #jogar novamente
        image02 = [pygame.image.load("assets/MenuScreen/Leaderboard.png").convert_alpha(), (275, 300)] #leaderboard
        image03 = [pygame.image.load("assets/MenuScreen/Sair.png").convert_alpha(), (275, 460)] #sair
        image04 = [pygame.image.load("assets/MenuScreen/VoltarMenu.png").convert_alpha(), (30, 30)]
        self.images.append(image)
        self.images.append(image01)
        self.images.append(image02)
        self.images.append(image03)
        self.images.append(image04)
        return self.images
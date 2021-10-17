import pygame, sys, os

class Map:

    def __init__(self):
        self.image = pygame.image.load("image_path.png").convert_alpha()
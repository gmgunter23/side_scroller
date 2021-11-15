import pygame, sys
from pygame.locals import *
import random, time

#initializing
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_LENGTH = 400
SPEED = 5

background = pygame.image.load("ocean.jpg")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("The Ocean")



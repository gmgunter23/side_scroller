#imports
import pygame, sys
from pygame.locals import *
import random, time

#Initializing
pygame.init()

#setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other variable for use in the progam
SCREEN_WIDTH = 1000
SCREEN_LENGTH = 700
SPEED = 5
SCORE = 0

#setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.transform.scale(pygame.image.load("ocean_2.jpg"), (SCREEN_WIDTH, SCREEN_LENGTH))

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("The Ocean") 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pirate_ship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center=(SCREEN_WIDTH, random.randint(30, SCREEN_LENGTH - 40))

    def move(self):
        global SCORE
        self.rect.move_ip(-SPEED, 0)
        if (self.rect.left < 0):
            SCORE += .5
            self.rect.top = 0
            self.rect.center = (SCREEN_WIDTH, random.randint(30, SCREEN_LENGTH - 40))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_boat.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) ########Search for warning
        self.rect = self.image.get_rect()
        self.rect.center = (40, 350)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
E2 = Enemy()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)


#Adding a new user event
INC_SPEED = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound("waves.mp3").play()
# Game loop
while True:

    #Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        sound_running = False
        pygame.mixer.Sound("boat_crash.mp3").play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
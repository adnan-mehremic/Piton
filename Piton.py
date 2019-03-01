# Python game "Piton"


import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Had {0} initializing erros, "
          "exiting".format(check_errors[1]))
    sys.exit(-1)

else:
    print("PyGame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Piton')

# Colors
red = pygame.Color(255, 0, 0) # for game over
green = pygame.Color(0, 255, 0) # for snake
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0) # for score
white = pygame.Color(255, 255, 255) # for background
brown = pygame.Color(165, 42, 42) # for food

# FPS controller
fpsController = pygame.time.Clock()

# Variables
snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

# game over function

def gameOver():
    myFont = pygame.font.SysFont('monaco', 70)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 20)
    playSurface.blit(GOsurf, GOrect)
    pygame.display.flip()

gameOver()
time.sleep(10)
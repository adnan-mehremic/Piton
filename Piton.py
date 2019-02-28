# Python game "Piton"


import pygame, sys, random, time

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

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
    time.sleep(4)
    pygame.quit()  # game exit
    pygame.exit()  # console exit

# Main Logic of the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'DOWN'
            if event.key == pygame.K_DOWN:
                changeto = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    # validation of direction

    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = "RIGHT"
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = "LEFT"
    if changeto == 'UP' and not direction == 'DOWN':
        direction = "UP"
    if changeto == 'DOWN' and not direction == 'UP':
        direction = "DOWN"

    # update snake position [x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] += 10
    if direction == 'DOWN':
        snakePos[1] -= 10

    # snake body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10,
                   random.randrange(1, 46) * 10]
        foodSpawn = True

    # Background
    playSurface.fill(white)

    # Draw snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(playSurface, brown,
                     pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()

    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()


    pygame.display.flip()
    fpsController.tick(23)








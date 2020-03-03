import pygame, sys, math, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
player = pygame.Rect(15,15,15,15)
vec = None
direction = None
target = 141, 250
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            target = pygame.mouse.get_pos()

    currentx = player.x
    currenty = player.y

    vec = (target[0] - currentx, target[1] - currenty)
    distance = math.sqrt(vec[0]**2 + vec[1]**2)
    print(distance)
    if(distance == 0):
        pass
    else:
        normalize = (vec[0]/round(distance), vec[1]/round(distance))
        direction = normalize
        print(normalize)
        print(direction)
    print(vec)
    speed_x = round(direction[0] * 5)
    speed_y = round(direction[1] * 5)

    player.x += speed_x
    player.y += speed_y



    #screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    clock.tick(60)
    pygame.display.update()
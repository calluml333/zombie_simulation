import sys
import pygame

pygame.init()

SIZE = 640, 480
screen = pygame.display.set_mode(SIZE)
FPSCLOCK = pygame.time.Clock()

startpoint = pygame.math.Vector2(320, 240)
endpoint = pygame.math.Vector2(170, 0)
angle = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    angle = (angle+5) % 360
    # The current endpoint is the startpoint vector + the 
    # rotated original endpoint.
    current_endpoint = startpoint + endpoint.rotate(angle)

    screen.fill((0, 0, 0))
    pygame.draw.line(
        screen, pygame.Color("red"), startpoint, current_endpoint, 2)

    pygame.display.flip()  
    FPSCLOCK.tick(30)

pygame.quit()
sys.exit(0)

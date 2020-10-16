### PyGame
import pygame
import time
## initialize
pygame.init()

screen = pygame.display.set_mode((1600,2800))
## RGB
running = True
while running:
    # time.sleep(1)
    screen.fill((255, 9, 34))
    pygame.draw.circle(screen, (0,255,0),(500,500), 350)
    pygame.draw.circle(screen, (0,0,235),(350,670), 250, 90)
    pygame.draw.polygon(screen, (255,0,255),[(0,5),(65,67),(44,3)],5)
    pygame.draw.polygon(screen,(15,67,94), [(700,800), (900,1000), (120,360), (790,980)], 8)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You just pressed X button!!!!")
            running = False

    pass
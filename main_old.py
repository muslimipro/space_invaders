import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

bg_image = pygame.image.load("space.jpg").convert()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg_image, [0, 0])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
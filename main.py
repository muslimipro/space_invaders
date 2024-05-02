import pygame

BLACK	= ( 0, 0, 0)
WHITE	= ( 255, 255, 255)
GREEN	= ( 0, 255, 0)
RED     = ( 255, 0, 0)
BLUE    = ( 0, 0, 255)

# pygame setup
pygame.init()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
# bkground_image = pygame.image.load("image.jpg")
running = True

x = 640 / 2 - 50

MOVE_RIGHT = 1
MOVE_LEFT = 2
DIRECTION = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:	
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:		
                DIRECTION=MOVE_LEFT
            elif event.key == pygame.K_RIGHT: 	
                DIRECTION=MOVE_RIGHT
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                DIRECTION=0		
            elif event.key==pygame.K_RIGHT:
                DIRECTION=0
    if DIRECTION==MOVE_LEFT:
        x-=5
    elif DIRECTION==MOVE_RIGHT:
        x+=5

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen,WHITE,[x,200,100,100])
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
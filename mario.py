import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

sprite = pygame.image.load("mario.png")
x=150
y=150

clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    pygame.event.pump()

    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_UP]:
        y = y - 20
    elif keyinput[pygame.K_DOWN]:
        y = y + 20
    elif keyinput[pygame.K_ESCAPE]:
        raise SystemExit

    screen.blit(background, (0,0))
    screen.blit(sprite, (x, y))
    pygame.display.flip()

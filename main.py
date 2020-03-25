import pygame
import targets

pygame.init()
icon = pygame.image.load('./icon.png')
pygame.display.set_icon(icon)

winSize = 750
res = (winSize, winSize)
win  = pygame.display.set_mode(res)
pygame.display.set_caption("Machinelearning Projekt")

width = 40
rad = int(width / 2)
x = int(winSize / 2) - rad
y = int(winSize / 2) - rad
vel = 10

run = True

targets.GetData(rad, x, y)
targets.Generate(winSize, rad / 2, 10)

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not x < (0 + rad - vel):
        x -= vel
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x < (0 + rad - vel):
        x = 750 - width

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not x > (winSize - width - vel):
        x += vel
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x > (winSize - width - vel):
        x = 0
    
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not y < (0 + rad - vel):
        y -= vel
    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and y < (0 + rad - vel):
        y = winSize - width

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not y > (winSize - width - vel):
        y += vel
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y > (winSize - width - vel):
        y = 0

    if keys[pygame.K_ESCAPE]:
        run = False

    win.fill((22, 22, 22))

    targets.GetData(rad, x, y)
    targets.Draw(win)

    pygame.draw.circle(win, (0, 255, 155), (x + rad, y + rad), rad)

    pygame.display.update()

pygame.quit()
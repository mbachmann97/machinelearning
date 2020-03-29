import pygame
import targets
import helper
import gameplay

pygame.init()
icon = pygame.image.load('./icon.png')
pygame.display.set_icon(icon)

winSize = 950
gameSize = 750
res = (winSize, gameSize)
win  = pygame.display.set_mode(res)
pygame.display.set_caption("Machinelearning Projekt")

gameoverTime = 30
TESTTIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TESTTIMER, gameoverTime * 1000)

width = 40
rad = int(width / 2)
x = int(gameSize / 2) - rad
y = int(gameSize / 2) - rad
vel = 10
mousePos = (0, 0)

run = True

targets.GetData(rad, x, y)
targets.Generate(gameSize, rad / 2, 10)

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == TESTTIMER:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    
    mods = pygame.key.get_mods()
    keys = pygame.key.get_pressed()

    showViewField = False

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not x < (0 + rad - vel):
        x -= vel
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x < (0 + rad - vel):
        x = gameSize - width

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not x > (gameSize - width - vel):
        x += vel
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x > (gameSize - width - vel):
        x = 0
    
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not y < (0 + rad - vel):
        y -= vel
    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and y < (0 + rad - vel):
        y = gameSize - width

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not y > (gameSize - width - vel):
        y += vel
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y > (gameSize - width - vel):
        y = 0

    if keys[pygame.K_SPACE]:
        showViewField = True
    else:
        showViewField = False

    if keys[pygame.K_ESCAPE]:
        run = False

    win.fill((22, 22, 22))

    if showViewField:
        pygame.draw.circle(win, (55, 55, 55), (x + rad, y + rad), 250 - int(rad / 2), 2)

    targets.GetData(rad, x, y)
    targets.Draw(win)

    pygame.draw.circle(win, (0, 255, 155), (x + rad, y + rad), rad)

    pygame.draw.rect(win, (40, 45, 91), (gameSize, 0, 200, gameSize))

    targets.DrawScore(win)

    gameplay.DrawTimer(win, gameoverTime)
    gameplay.DrawStartButton(win, gameSize, winSize, mousePos)

    pygame.display.update()

pygame.quit()
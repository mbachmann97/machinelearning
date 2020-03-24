import pygame
import math
from random import random

pygame.init()

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

targets = []
for i in range(10):
    w = math.trunc(random() * 10000 % winSize)
    h = math.trunc(random() * 10000 % winSize)

    if winSize < (w + int(rad / 2)):
        w = w - int(rad / 2)
    elif int(rad / 2) > w:
        w = w + int(rad / 2)

    if winSize < (y + int(rad / 2)):
        y = y - int(rad / 2)
    elif int(rad / 2) > w:
        y = y + int(rad / 2)

    targets.append((w, h))

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

    win.fill((22, 22, 22))
    
    for target in targets:
        pygame.draw.line(win, (255, 255, 0), target, (x + rad, y + rad), 2)
        pygame.draw.circle(win, (255, 255, 255), target, int(rad / 2))

    pygame.draw.circle(win, (0, 255, 155), (x + rad, y + rad), rad)

    pygame.display.update()

pygame.quit()
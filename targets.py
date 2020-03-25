import pygame
import helper

targets = []
radius = 0
playerX = 0
playerY = 0
d = 0

def GetData(_playerRadius, _playerX, _playerY):
    global radius, playerX, playerY
    radius  = int(_playerRadius / 2)
    playerX = _playerX
    playerY = _playerY

def Generate(winSize, radius, count):
    for i in range(10):
        w = helper.Rand(winSize)
        h = helper.Rand(winSize)

        if winSize < (w + int(radius)):
            w = w - int(radius)
        elif int(radius) > w:
            w = w + int(radius)

        if winSize < (h + int(radius)):
            h = h - int(radius)
        elif int(radius) > w:
            h = h + int(radius)

        distance = helper.Distance((w, h), (playerX, playerY), int(radius * 2))

        targets.append([(w, h), distance])

def Draw(targetWindow):
    DrawRangeLines(targetWindow)
    DrawTargets(targetWindow)

#~~ INTERNAL ~~#

def DrawRangeLines(targetWindow):
    for target in targets:
        target[1] = helper.Distance(target[0], (playerX, playerY), int(radius * 2))

        if target[1] < 250:
            pygame.draw.line(targetWindow, (255, 255, 0), target[0], (playerX + int(radius * 2), playerY + int(radius * 2)), 2)

def DrawTargets(targetWindow):
    for target in targets:
        pygame.draw.circle(targetWindow, (255, 255, 255), target[0], radius)
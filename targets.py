import pygame
import helper

targets = []
radius = 0
playerX = 0
playerY = 0
score = 0

def GetData(_playerRadius, _playerX, _playerY):
    global radius, playerX, playerY
    radius  = int(_playerRadius / 2)
    playerX = _playerX
    playerY = _playerY

def Generate(winSize, radius, count):
    for i in range(20):

        valid = False

        while valid == False:

            w = helper.Rand(winSize)
            h = helper.Rand(winSize)

            if winSize < (w + int(radius)):
                w = w - int(radius)
            elif int(radius) > w:
                w = w + int(radius)

            if winSize < (h + int(radius)):
                h = h - int(radius)
            elif int(radius) > h:
                h = h + int(radius)

            if len(targets) > 0:
                isInvalidToAtleastOne = False
                for target in targets:
                    distance = helper.Distance((w, h), target[0], 0)
                    if distance < ((radius + 2.5) * 2):
                        isInvalidToAtleastOne = True
                if isInvalidToAtleastOne:
                    valid = False
                else:
                    valid = True
            else:
                valid = True

        distanceToPlayer = helper.Distance((w, h), (playerX, playerY), int(radius * 2))
        targets.append([(w, h), distanceToPlayer])

def Draw(targetWindow):
    DrawRangeLines(targetWindow)
    DrawTargets(targetWindow)

def DrawScore(targetWindow):
    helper.RenderText(targetWindow, 'Consolas', 20, "Score: " + str(score), (255, 255, 255), (750, 30), (10, 0))

#~~ INTERNAL ~~#

def DrawRangeLines(targetWindow):
    for target in targets:
        target[1] = helper.Distance(target[0], (playerX, playerY), int(radius * 2))

        if target[1] < (radius + int(radius * 2)):
            global score
            score += 1
            targets.remove(target)
        elif target[1] < 250:
            pygame.draw.aaline(targetWindow, (255, 255, 0), target[0], (playerX + int(radius * 2), playerY + int(radius * 2)), 2)

def DrawTargets(targetWindow):
    for target in targets:
        pygame.draw.circle(targetWindow, (255, 255, 255), target[0], radius)

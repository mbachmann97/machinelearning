import pygame
import helper

def DrawStartButton(targetWindow, gameSize, winSize, mousePos):
    if (mousePos[0] > gameSize and mousePos[0] < winSize) and (mousePos[1] > (gameSize - 80) and mousePos[1] < (gameSize - 30)):
        pygame.draw.rect(targetWindow, (0, 255, 155), (gameSize, gameSize - 80, winSize - gameSize, 50))
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
    else:
        pygame.draw.rect(targetWindow, (255, 255, 255), (gameSize, gameSize - 80, winSize - gameSize, 50))
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
    helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 16, "Start", (33, 33, 33), (850, gameSize - 66), (0, 0), True)

def DrawTimer(targetWindow, gameoverTime):
    time = str(pygame.time.get_ticks())
    cutTime = 0
    if len(time) == 4:
        cutTime = time[:1]
    elif len(time) == 5:
        cutTime = time[:2]
    timer = str(gameoverTime - int(cutTime))
    if len(timer) == 0:
        timer = '0'
    helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 26, timer + "s", (255, 255, 255), (850, 95), (0, 0), True)
    helper.RenderText(targetWindow, './fonts/RobotoMono-Italic.ttf', 16, "verbleibend", (255, 255, 255), (850, 125), (0, 0), True)
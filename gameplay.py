import pygame
import helper
import targets

gameSizeG = 0
winSizeG = 0
timerActive = False
ignoredTime = 0

def DrawStartButton(targetWindow, gameSize, winSize, mousePos):
    global gameSizeG, winSizeG
    gameSizeG = gameSize
    winSizeG =  winSize
    if (mousePos[0] > gameSize and mousePos[0] < winSize) and (mousePos[1] > (gameSize - 80) and mousePos[1] < (gameSize - 30)):
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        if timerActive is False:
            pygame.draw.rect(targetWindow, (0, 255, 155), (gameSize, gameSize - 80, winSize - gameSize, 50))
            helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 16, "Start", (33, 33, 33), (850, gameSize - 66), (0, 0), True)
        else:
            pygame.draw.rect(targetWindow, (255, 100, 100), (gameSize, gameSize - 80, winSize - gameSize, 50))
            helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 16, "Stop", (33, 33, 33), (850, gameSize - 66), (0, 0), True)
    else:
        pygame.draw.rect(targetWindow, (255, 255, 255), (gameSize, gameSize - 80, winSize - gameSize, 50))
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        if timerActive is False:
            helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 16, "Start", (33, 33, 33), (850, gameSize - 66), (0, 0), True)
        else:
            helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 16, "Stop", (33, 33, 33), (850, gameSize - 66), (0, 0), True)

def DrawTimer(targetWindow, gameoverTime):
    if timerActive:
        time = str(pygame.time.get_ticks() - ignoredTime)
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
    else:
        helper.RenderText(targetWindow, './fonts/RobotoMono-Regular.ttf', 26, "30s", (255, 255, 255), (850, 95), (0, 0), True)
        helper.RenderText(targetWindow, './fonts/RobotoMono-Italic.ttf', 16, "verbleibend", (255, 255, 255), (850, 125), (0, 0), True)

def OnStartButtonClick(mousePos, TESTTIMER, gameoverTime):
    global timerActive, ignoredTime
    if (mousePos[0] > gameSizeG and mousePos[0] < winSizeG) and (mousePos[1] > (gameSizeG - 80) and mousePos[1] < (gameSizeG - 30)) and timerActive is not True:
        print("Start Button Click!")
        pygame.time.set_timer(TESTTIMER, gameoverTime * 1000, True)
        ignoredTime = pygame.time.get_ticks()
        timerActive = True
    elif (mousePos[0] > gameSizeG and mousePos[0] < winSizeG) and (mousePos[1] > (gameSizeG - 80) and mousePos[1] < (gameSizeG - 30)) and timerActive is True:
        ResetGame()

def ResetGame():
    global timerActive
    timerActive = False
    targets.ResetTargets()
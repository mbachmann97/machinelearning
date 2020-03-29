from random import random
import math
import pygame

def Rand(max):
    return math.trunc(random() * 10000 % max)

def Distance(circle1, circle2, radius):
    # sqrt( (x2 − x1)² + (y2 − y1)² )
    return math.sqrt(((circle1[0] - (circle2[0] + radius)) ** 2) + ((circle1[1] - (circle2[1] + radius)) ** 2))

def RenderText(screen, font, size, text, color, position, margin, isCenter=False):
    font = pygame.font.Font(font, size)
    output = font.render(text, True, color)
    if isCenter:
        finalPos = ((position[0] + margin[0]) - int(output.get_rect()[2] / 2), position[1] + margin[1])
    else:
        finalPos = (position[0] + margin[0], position[1] + margin[1])
    screen.blit(output, finalPos)
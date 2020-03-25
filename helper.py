from random import random
import math

def Rand(max):
    return math.trunc(random() * 10000 % max)

def Distance(circle1, circle2, radius):
    # sqrt( (x2 − x1)² + (y2 − y1)² ) 
    return math.sqrt(((circle1[0] - (circle2[0] + radius)) ** 2) + ((circle1[1] - (circle2[1] + radius)) ** 2))
import random
import settings
from . import Developers

developers = Developers.developers
poolNavigators = []

def draftNavigator(driver):
    global gblDriver

    gblDriver = driver

    populatePoolNavigators()
    return random.choice(poolNavigators)

def populatePoolNavigators():
    if gblDriver.experience == 'Estagiario':
        settings.setProbabilities(0.0 , 0.2 , 0.4 , 0.4)
    elif gblDriver.experience == 'Junior':
        settings.setProbabilities(0.05 , 0.05 , 0.15 , 0.75)
    elif gblDriver.experience == 'Pleno':
        settings.setProbabilities(0.4 , 0.3 , 0.1 , 0.2)
    else:
        settings.setProbabilities(0.2 , 0.6 , 0.15 , 0.05)

    for dev in developers:
        if canIAdd(dev):
            poolNavigators.append(dev)
            settings.added[dev.experience] += 1

def canIAdd(dev):
    condition = dev != gblDriver and not settings.devInPairs(dev)
    condition = condition and settings.added[dev.experience] < developers.__len__() * settings.probabilities[dev.experience]

    return condition

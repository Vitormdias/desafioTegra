import random
from . import Developers
import settings

developers = Developers.developers

poolDrivers = []

def draftDriver():
    populatePoolDrivers()
    return random.choice(poolDrivers)

def populatePoolDrivers():
    poolDrivers.clear()
    settings.setProbabilities(0.4 , 0.4 , 0.1 , 0.1)

    for dev in developers:
        if canIAdd(dev):
            poolDrivers.append(dev)
            settings.added[dev.experience] += 1


def canIAdd(dev):
    return settings.added[dev.experience] < developers.__len__() * settings.probabilities[dev.experience] and not settings.devInPairs(dev)

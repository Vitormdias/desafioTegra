import random
from . import Developers
import settings

developers = Developers.developers

poolDrivers = []

def draftDriver():
    populatePoolDrivers()

    try:
        return random.choice(poolDrivers)
    except Exception as e:
        print("No developers available")

def populatePoolDrivers():
    poolDrivers.clear()
    
    global added
    added = settings.setAdded()

    for dev in developers:
        if canIAdd(dev):
            poolDrivers.append(dev)
            added[dev.experience] += 1


def canIAdd(dev):
    probabilities = settings.setProbabilities(0)

    devProb = developers.__len__() * probabilities[dev.experience-1]

    conditions = []

    conditions.append(not settings.devInPairs(dev))
    conditions.append(added[dev.experience] < devProb)

    return sum(conditions) == conditions.__len__()

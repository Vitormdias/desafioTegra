import random
import settings
import sys
from . import Developers

developers = Developers.developers
poolNavigators = []

def draftNavigator(driver):
    global gblDriver

    gblDriver = driver

    populatePoolNavigators()

    try:
        return random.choice(poolNavigators)
    except Exception as e:
        print("No developers available")


def populatePoolNavigators():
    poolNavigators.clear()

    global added
    added = settings.setAdded()

    for dev in developers:
        if  canIAdd(dev):
            added[dev.experience] += 1
            poolNavigators.append(dev)

def canIAdd(dev):
    probabilities = settings.setProbabilities(dev.experience)

    devProb = developers.__len__() * probabilities[dev.experience - 1]

    conditions = []

    conditions.append(dev != gblDriver)
    conditions.append(not settings.devInPairs(dev))
    conditions.append(added[dev.experience] < devProb)

    return sum(conditions) == conditions.__len__()

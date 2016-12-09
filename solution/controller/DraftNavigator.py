import random
from . import Developers

developers = Developers.developers
poolNavigators = []

added = {}
probabilities = {}

def draftNavigator(driver):
    global gblDriver

    gblDriver = driver

    populatePoolNavigators()
    return random.choice(poolNavigators)

def populatePoolNavigators():
    if gblDriver.experience == 'estagiario':
        setProbabilities(0.0 , 0.2 , 0.4 , 0.4)
    elif gblDriver.experience == 'junior':
        setProbabilities(0.05 , 0.05 , 0.15 , 0.75)
    elif gblDriver.experience == 'pleno':
        setProbabilities(0.4 , 0.3 , 0.1 , 0.2)
    else:
        setProbabilities(0.2 , 0.6 , 0.15 , 0.05)

    for dev in developers:
        if canIAdd(dev):
            poolNavigators.append(dev)
            added[dev.experience] += 1

def canIAdd(dev):
    condition = dev != gblDriver #and dev not in pairs
    condition = condition and added[dev.experience] < developers.__len__() * probabilities[dev.experience]

    return condition

def setProbabilities(eP , jP , pP , sP):
    probabilities['estagiario'] = eP
    probabilities['junior'] = jP
    probabilities['pleno'] = pP
    probabilities['senior'] = sP

    added['estagiario'] = 0
    added['junior'] = 0
    added['pleno'] = 0
    added['senior'] = 0

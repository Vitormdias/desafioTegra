import random
from . import Developers

developers = Developers.developers

poolDrivers = []

added = {}
probabilities = {}

def draftDriver():
    populatePoolDrivers()
    return random.choice(poolDrivers)

def populatePoolDrivers():
    setProbabilities(0.4 , 0.4 , 0.1 , 0.1)

    for dev in developers:
        if canIAdd(dev):
            poolDrivers.append(dev)
            added[dev.experience] += 1


def canIAdd(dev):
    return added[dev.experience] < developers.__len__() * probabilities[dev.experience] #and dev not in pairs

def setProbabilities(eP , jP , pP , sP):
    probabilities['estagiario'] = eP
    probabilities['junior'] = jP
    probabilities['pleno'] = pP
    probabilities['senior'] = sP

    added['estagiario'] = 0
    added['junior'] = 0
    added['pleno'] = 0
    added['senior'] = 0

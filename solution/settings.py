pairs = []
probabilities = []
added = []

options = {}

probabilities.append([0.4 , 0.4 , 0.1 , 0.1])
probabilities.append([0.0 , 0.2 , 0.4 , 0.4])
probabilities.append([0.05 , 0.05 , 0.15 , 0.75])
probabilities.append([0.4 , 0.3 , 0.1 , 0.2])
probabilities.append([0.2 , 0.6 , 0.15 , 0.05])

def setProbabilities(exp):
    return probabilities[exp]

def setAdded():
    added = [0] * (options.__len__()+1)
    return added

def devInPairs (dev):
    for p in pairs:
        if dev == p.driver or dev == p.navigator:
            return True
    return False

def setOptions(ops):
    index = 1
    for op in ops:
        options[index] = op
        index += 1

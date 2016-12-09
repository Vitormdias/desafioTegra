pairs = []

added = {}
probabilities = {}

def setProbabilities(eP , jP , pP , sP):
    probabilities['Estagiario'] = eP
    probabilities['Junior'] = jP
    probabilities['Pleno'] = pP
    probabilities['Senior'] = sP

    added['Estagiario'] = 0
    added['Junior'] = 0
    added['Pleno'] = 0
    added['Senior'] = 0

def devInPairs (dev):
    for p in pairs:
        if dev == p.driver or dev == p.navigator:
            return True
    return False

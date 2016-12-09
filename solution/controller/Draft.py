from classes.Pair import Pair
from . import DraftDriver
from . import DraftNavigator

pairs = []

def draft():

    driver = DraftDriver.draftDriver()
    navigator = DraftNavigator.draftNavigator(driver)

    pair = Pair(driver , navigator)

    pairs.append(pair)

    print (pair.presentation())

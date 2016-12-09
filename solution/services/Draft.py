from models.Pair import Pair
from . import DraftDriver
from . import DraftNavigator
import settings

def draft():

    driver = DraftDriver.draftDriver()
    navigator = DraftNavigator.draftNavigator(driver)

    pair = Pair(driver , navigator)

    settings.pairs.append(pair)

    try:
        print (pair.presentation())
    except Exception as e:
        print("Draft aborted")

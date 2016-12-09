class Pair():
    def __init__(self , driver , navigator):
        self.driver = driver
        self.navigator = navigator

    def presentation(self):
        return "Driver: {0!s} Navigator: {1!s}".format(self.driver.name , self.navigator.name)

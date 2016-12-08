class Pair():
    def __init__(self , driver , navigator):
        self.driver = driver
        self.navigator = navigator

    def presentation(self):
        return "{0!s} eh o Driver e {1!s} eh o Navigator".format(self.driver.name , self.navigator.name)

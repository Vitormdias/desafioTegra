class Developer():
    def __init__ (self , name,experience):
        self.name = name.lower()
        self.experience = experience.lower()

    def presentation(self):
        return "Ola sou {0!s} e sou um {1!s}".format(self.name ,self.experience)

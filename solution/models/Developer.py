class Developer():
    def __init__ (self , name,experience):
        self.name = name.capitalize()
        self.experience = experience.capitalize()

    def presentation(self):
        return "Name: {0!s} Experience: {1!s}".format(self.name ,self.experience)

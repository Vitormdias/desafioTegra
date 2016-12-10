import settings

class Developer():
    def __init__ (self , name, experience):
        self.name = name.capitalize()
        self.experience = experience

    def presentation(self):
        return "Name: {0!s} Experience: {1!s}".format(self.name , settings.options[self.experience])

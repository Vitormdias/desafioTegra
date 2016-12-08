class Developer():
    def __init__ (self , name,experience):
        self.name = name
        self.experience = experience

    def presentation(self):
        return "Hello I am {0!s} and I am a {1!s}".format(self.name ,self.experience)

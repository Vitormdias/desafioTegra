from models.Developer import Developer

developers = []

def addDev(name , function):
    developer = Developer(name , function)

    developers.append(developer)

    print (developer.presentation())

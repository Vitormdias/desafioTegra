from models.Developer import Developer

developers = []

def addDev(name , function):
    developer = Developer(name , function)

    developers.append(developer)

def show():
    for dev in developers:
        print (dev.presentation())

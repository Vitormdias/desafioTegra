from services import Developers
from services import Draft
from subprocess import call
import settings

def add():
    print('Name: ')
    name = str(input())

    print('Experience: ')
    print ("\tSelect an Option")
    print ("\t\t\t1 - Estagiario")
    print ("\t\t\t2 - Junior")
    print ("\t\t\t3 - Pleno")
    print ("\t\t\t4 - Senior")
    selectedOption = int(input())

    function = settings.options[selectedOption]

    Developers.addDev(name , function)

print ("\t\t\tPair Programming Draft")

if __name__ == '__main__':
    ops = ['Estagiario' , 'Junior' , 'Pleno' , 'Senior']
    settings.setOptions(ops)
    while(True):
        print ("\tSelect an Option")
        print ("\t\t\t1 - Add Developer")
        print ("\t\t\t2 - Draft Me A Pair")
        print ("\t\t\t3 - Let's Put Our Hands On")

        option = int(input())

        if option == 1:
            add()
        elif option == 2:
            Draft.draft()
        else:
            call(['clear'])
            print ("\t\t\tGo Commit Something!")
            exit()

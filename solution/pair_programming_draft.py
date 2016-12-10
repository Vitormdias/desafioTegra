from services import Developers
from services import Draft
from subprocess import call
import settings

global ops

def add():
    print('Name: ')
    name = str(input())

    print('Experience: ')
    print ("\tSelect an Option")

    it = 1
    for op in ops:
        print ("{0} - {1!s}".format(it , op))
        it += 1
        
    function = int(input())

    Developers.addDev(name , function)

print ("\t\t\tPair Programming Draft")

if __name__ == '__main__':
    ops = ['Estagiario' , 'Junior' , 'Pleno' , 'Senior']
    options = settings.setOptions(ops)
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

from services import Developers
from services import Draft
from subprocess import call


def add():
    print('Name: ')
    name = str(input())
    print('Function: ')
    function = str(input())

    Developers.addDev(name , function)
    Developers.show()

print ("\t\t\tPair Programming Draft")

if __name__ == '__main__':
    while(True):
        print ("\tSelect a Option")
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

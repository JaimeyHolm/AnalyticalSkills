import random

def Binair_Zoeken(target, lst):
    links = 0
    rechts = len(lst) - 1
    while links <= rechts:
        midden = round((links + rechts) / 2)
        if lst[midden] < target:
            links = midden + 1
        elif lst[midden] > target:
            rechts = midden - 1
        elif lst[midden] == target:
            return midden


def random_lijst():
    lijst = []
    i = random.randint(5, 17)
    while i != 0:
        getal = random.randint(1, 99)
        if getal not in lijst:
            lijst.append(getal)
            i -= 1
    return lijst


def test():
    i = 5
    while i != 0:
        lst = random_lijst()
        target = random.randint(1, 99)
        print('Random lijst: ' + str(lst))
        print('Target: ' + str(target))
        print(target in lst, '\n')
        i -= 1


test()

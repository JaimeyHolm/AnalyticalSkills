import random

def Lineair_Zoeken(target, lst):
    if len(lst) == 1 and target != lst[0]:
        return False
    elif lst[0] == target:
        return True
    else:
        return Lineair_Zoeken(target, lst[1:])


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

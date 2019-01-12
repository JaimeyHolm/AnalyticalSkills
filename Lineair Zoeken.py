import random

def Lineair_Zoeken(target, lst):
    if len(lst) == 1 and target != lst[0]:                  # Als de lijst nog 1 item heeft en dit niet de target is
        return False                                        # Geef niet terug
    elif lst[0] == target:                                  # Als de 1ste item van lijst het target is
        return True                                         # Geef wel terug
    else:
        return Lineair_Zoeken(target, lst[1:])               # Recursie met lijst zonder eerste item


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

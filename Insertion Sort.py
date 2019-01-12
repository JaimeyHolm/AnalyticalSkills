import random


def my_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key
    return lst


def random_lijst():
    lijst = []
    i = random.randint(5, 17)
    while i != 0:
        lijst.append(random.randint(1, 99))
        i -= 1
    return lijst


def test():
    i = 5
    while i != 0:
        lijst = random_lijst()
        print('Random lijst ongesorteerd: ' + str(lijst))
        print('Random lijst gesorteerd:   ' + str(my_sort(lijst)) + '\n')
        i -= 1


print(test())

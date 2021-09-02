import random
def rgen():
    a = 10
    b = 0
    c = 10
    list1 = []
    list2 = []
    for i in range(a):
        list1.append(random.randint(b, c))
        list2.append(random.randint(b, c))
    print("Случайный список 1: ", list1)
    print("Случайный список 2: ", list2)

    newlist = {x for x in list1 if x in list2}
    print("Список с общими значениями: ", newlist)

rgen()






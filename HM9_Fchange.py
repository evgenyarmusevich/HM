import random
a = int(input("Введите длину списка: "))
b = int(input("Введите минимальное значение списка: "))
c = int(input("Введите максимальное значение списка: "))
list1 = []

def rgen():
    for i in range(a):
        if b < c:
            list1.append(random.randint(b, c))
        else:
            list1.append(random.randint(c, b))
    print(list1)

def nfunc():
    list2 = list1.copy()
    cnum = int(input("Введите число от 0 до " + str(a - 1) + " "))
    if cnum >= a:
        print("Введенное число выходит за пределы списка!")
        nfunc()
    else:
        list1.pop(cnum)
        list1.insert(cnum, cnum)
        print("Модифицированный список " + str(list1))
        print("Число " + str(list2[cnum]) + " замененно на " + str(cnum))


rgen(), nfunc()
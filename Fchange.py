import random
def rgen():
    a = 10
    b = int(input("First nuber:"))
    c = int(input("Second number:"))
    list = []
    for i in range(a):
        if b < c:
            list.append(random.randint(b, c))
        else:
            list.append(random.randint(c, b))

    print(list)

    cnum = int(input("Third nuber:"))
    maxl = list.index(max(list))
    list[maxl] = cnum
    print(list)


rgen()
import random
def rgen(llength, lbottom, ltop):
    list1 = []
    for i in range(llength):
        if lbottom < ltop:
            list1.append(random.randint(lbottom, ltop))
        else:
            list1.append(random.randint(ltop, lbottom))
    return list1






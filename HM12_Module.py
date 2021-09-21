import mymodule
c = int(input("Длина списка: "))
b = int(input("Нижняя граница: "))
d = int(input("Верхняя граничца: "))
a1 = mymodule.rgen(c, b, d)
a2 = mymodule.rgen(c, b, d)
print(a1, a2)
newlist = {x for x in a1 if x in a2}
print("Список с общими значениями: ", list(newlist))


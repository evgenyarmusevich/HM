import random

def rgen():
    for i, j in enumerate(list):
        if j == num:
            print("Число " + str(num) + " находится в списке под номером " + str(i + 1))

a = 10
b = 1

list = []
for i in range(a):
    list.append(random.randint(b, a))
print("Список:", list)

num = int(input("Какое число необходимо найти? "))

if num > a:
    print("Числа " + str(num) + " нет в списке")

rgen()
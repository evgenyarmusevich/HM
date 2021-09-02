def count():
listn=str(input("Введите число: "))
print(listn)
k=0
for elem in listn:
    if not elem.isdigit():
        print("Введенные данные не являются числом")
        break
    if elem.isdigit():
        k += int(elem)
print("Сумма чисел =", k)

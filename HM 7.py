def func_1():
    a = int(input("Введите значение 'A' "))
    b = int(input("Введите значение 'B' "))
    c = int(input("Введите значение 'C' "))
    while a < b:
        print("Число " + str(a) + " меньше " + str(b))
        a = a + c
        if a >= b:
            print("Поздравляем, цикл завершен. Число " + str(a) + " равно или больше " + str(b))
            break


func_1()
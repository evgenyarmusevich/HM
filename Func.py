def my_function():
    a = int(input("переменная 'a':"))
    b = int(input("переменная 'b':"))
    print("сложение чисел =", (a + b),"\n" 
          "вычитание чисел =", (a - b), "\n"
          "умножение чисел =", (a * b), "\n"
          "деление чисел (целое) =", int(a / b), "\n"
          "деление чисел (с плавающей запятой) =", (a / b))

my_function()

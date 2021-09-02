a = input('Введите улицу: ')
b = input("Введите номер дома: ")
thisdict = {
  a:b
}
def dict():
    print(thisdict)
    for x, y in thisdict.items():
        print(x + ", " + y)

dict()

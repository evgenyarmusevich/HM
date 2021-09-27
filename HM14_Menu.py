from tkinter import *

main_menu = Menu()

file_menu = Menu()
def zagl():
    print("В разработке")
file_menu.add_command(label="Создать запись", command=zagl)
file_menu.add_command(label="Найти запись", command=zagl)
file_menu.add_command(label="Редактировать запись", command=zagl)
file_menu.add_command(label="Удалить запись", command=zagl)
file_menu.add_command(label="Выйти из программы", command=zagl)

main_menu.add_cascade(label="Главное меню", menu=file_menu)

from tkinter import *

main_menu = Menu()

file_menu = Menu()

file_menu.add_command(label="Создать запись")
file_menu.add_command(label="Найти запись")
file_menu.add_command(label="Редактировать запись")
file_menu.add_command(label="Удалить запись")
file_menu.add_command(label="Выйти из программы")

main_menu.add_cascade(label="Главное меню", menu=file_menu)
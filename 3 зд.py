# import os
# print("Текущая деректория:", os.getcwd())
# os.mkdir("folder")   # создать папку
# os.rmdir("folder")   # удалить папку

# Создать файл 'task_1.txt'
# f = open('task_1.txt', 'w') # открытие в режиме записи несуществующего файла

# #  Переименовать на renamefile.txt
import os
os.rename('task_1.txt', 'renamefile.txt')

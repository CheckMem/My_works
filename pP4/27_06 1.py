
# import pickle  #pickling - засолка, консервация данных, сериализация или десериализация
#
#
# fname = 'info.txt'
#
# with input('Введите слово для перевода:')
# d= {}
#
# if word in d:
#     print('Выводим перевод')
# else:
#     print('не знаю, но можете мне подсказать')
#     print('Как переводится', word)
#     new_word = input('')
#
#
#     d = pickle.load(file)
#
#
# print (d)















# import pickle  #pickling - засолка, консервация данных, сериализация или десериализация
#
#
# fname = 'info.txt'
#
# with open(fname, 'rb') as file:
#     d = pickle.load(file)
#
#
# print (d)


















# import os
# root = os.getcwd()
# fname = 'info.txt'
#
# list_1 = [1,3,5,8,12,24,37,55,89]
# list_2 = [2,4,5,8,14,24,39,58,89]
#
# temp = []
#
# for item in list_1:
#         if item in list_2:
#                 temp.append(item)
#
#
#
# if os.path.isfile(fname):
#         with open(fname, 'wt', encoding='utf-8') as file:
#              print(*temp, sep=', ', file=file)



# import os
# root = os.getcwd()
# fname = 'info.txt'
#
# list_1 = [1,3,5,8,12,24,37,55,89]
# list_2 = [2,4,5,8,14,24,39,58,89]
#
# set1= set(list_1)
# set2= set(list_2)
# temp = set1.intersection(set2)
#
#
#
# if os.path.isfile(fname):
#         with open(fname, 'wt', encoding='utf-8') as file:
#              print(*temp, sep=', ', file=file)


















# #теперь печатает всё внутрь файла инфо, т. е. write
#
# import os
# root = os.getcwd()
#
# string =''
# fname = 'info.txt'
# if os.path.isfile(fname):
#         file = open(fname, 'rt', encoding='utf-8') #есть такая вещь как указатель at от append
#         s = file.readline()
#         while s != '':
#                 string += s
#                 s = file.readline()
#
#                 file.close()
#
#                 res = s.splitlines()
#                 print(res)














# #считывание цифр из файла
#
# import os
# root = os.getcwd()
#
# fname = 'info.txt'
# if os.path.isfile('info.txt'):
#         file = open('info.txt', 'rt', encoding='utf-8') #есть такая вещь как указатель at от append
#         print('Имя файла:',file.name)
#         print('Режим:',file.mode)
#         print('Кодировка:',file.encoding)
#
#         string = file.read() #123
#         lst = list(string)
#         summ = 0
#
#         file.close()
#         for i in lst:
#                 if i.isdigit():
#                      summ += int(i)
#         print(summ)
#
# else:
#    print('Файл не существует!')
#
# #должен печатать то что в инфо






























# import os
# root = os.getcwd()
# if os.path.isfile('info.txt'):
#         file = open('info.txt', 'rt', encoding='utf-8') #есть такая вещь как указатель at от append
#         print('Имя файла:',file.name)
#         print('Режим:',file.mode)
#         print('Кодировка:',file.encoding)
#
#         file.read(3)
#         text1 = file.read(4)
#         file.read(2)
#         text2 = file.read(7)
#
#         file.close()
#         print(f'A {text1}-to {text2}')
#
# else:
#    print('Файл не существует!')
#
# #должен печатать то что в инфо

























# import os
# root = os.getcwd()
# file = open('info.txt', 'rt') #есть такая вещь как указатель at от append
# print('Имя файла:',file.name)
# print('Режим:',file.mode)
# print('Кодировка:',file.encoding)
#
# res = file.read(2)
# temp = file.read(5)
#
# file.close()
# print('Файл на диске',res)
# print(temp)






# import os
# root = os.getcwd()
# file = open('info.txt', 'at') #есть такая вещь как указатель at от append
# print('Имя файла:',file.name)
# print('Режим:',file.mode)
# print('Кодировка:',file.encoding)
#
# res = file.write(root)
# file.close()
# print(res)



# import os
#
#
# root = os.getcwd()
#
# file = open('info.txt', 'wt')
# print('Имя файла:',file.name)
# print('Режим:',file.mode)
# print('Кодировка:',file.encoding)
#
# file.write(root)
#
#
# file.close()



















# import os
#
# root = os.getcwd()  #где мой скрипт?
#
# if not os.path.isdir('images'):   #если такой директории нет, то создать
#     os.mkdir('images') #создали dir "images"
#
# files = os.listdir(root)
# images = [] #пока пустой список для файлов изображений
#
# for file in files:
#     if os.path.isfile(file) and \
#             (file.endswith('.png')
#              or file.endswith('.jpg')):
#         images.append(file)
#
# os.replace - перемещение
# os.remove - удаление
# os.rename - переименовать
# os.walk()- рекурсивный обход всех папок по заданному пути


























# import os
#
# root = os.getcwd()  #где мой скрипт?
#
# if not os.path.isdir('images'):   #если такой директории нет, то создать
#     os.mkdir('images') #создали dir "images"
#
# files = os.listdir(root)
# images = [] #пока пустой список для файлов изображений
#
# for file in files:
#     if os.path.isfile(file) and \
#             (file.endswith('.png')
#              or file.endswith('.jpg')):
#         images.append(file)
# for image in images:
#     os.replace(image, 'images/' + image)











# https://all-python.ru/osnovy/os.html?ysclid=ljdywbygw683065640





# Возможности модуля os позволяют не только отображать
# информацию об уже существующих в памяти объектах, но
# и генерировать абсолютно новые. Например, с помощью метода
# mkdir довольно легко создать папку, просто указав для нее желаемый путь.
# В следующем примере в корневом каталоге диска D производится новая папка под названием folder через mkdir
# import os
# os.mkdir(r"D:\folder")




# import os
#
# root =os.getcwd()  #где мой скрипт?
# print('Мы пока здесь:',root)
# if not os.path.isdir('images'):   #если такой директории нет, то создать
#     os.mkdir('images') #создали dir "images"
# os.chdir('images')   #меняем директории на images
# print('А теперь здесь:', os.getcwd())
# os.chdir('..') # (root) вверх на один уровень
# print('Мы снова здесь:',root)


















#По умолчанию рабочей директорией программы является каталог,
# где содержится документ с ее исходным кодом. Благодаря
# этому, можно не указывать абсолютный путь к файлу, если тот
# находится именно в этой папке. Получить сведения о текущей директории
# позволяет функция getcwd, которая возвращает полный адрес рабочего каталога
# на жестком диске. В следующем фрагменте кода показано что будет, если передать
# результат работы этого метода в print. Как можно заметить, рабочей директорией
# является каталог program на системном диске C.

# import os
#
# path =os.getcwd()
#
# print(type(path))
















#Получить сведения, которые касаются конфигурации компьютера,
# можно при помощи метода environ. Вызвав его через обращение к библиотеке os,
# пользователь получает большой словарь с переменными окружения,
# который выводится в консоль или строковую переменную.
# Таким образом, можно узнать название системного диска,
# адрес домашней директории, имя системы и массу другой информации.
# Следующий пример демонстрирует применение environ.

# import os
#
# print(os.environ)











# import os
#
# print(os.name)
























# закончили дрочиво с continue продолжаем тему с файлами

# counter = 0
#
# while True:
#     counter += 1
#     if counter > 10:
#         break
#     if counter % 10 == 5:
#         continue
#     print(counter)
#
# print('Цикл прерван')
#














# counter = 0
#
# while True:
#     counter += 1
#     if counter > 10:
#         break
#     if counter % 2:
#         continue
#     print(counter)
#
# print('Цикл прерван')


















# #считает до 10
# counter = 0
#
# while True:
#     counter += 1
#     if counter > 10:
#         break
#     print(counter)








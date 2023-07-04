
# #a = [ i for i in range(101) if i % 10 == 5]
#
# ip = '198.162.100.101'
#
# a = [int(i) for i in ip.split('.')]
# print(sum(a))
#
#
#
#
# a = ip.split('.')
#
# summ = 0
# for i in a:
#     summ += int(i)
#
# print(summ)








# a = [ i for i in range(1, 11)]
#
# print(a)






# a = []
#
# for i in range(1, 11):
#     a.append(i)
#
# print(a)















# name = 'Виктор'
# age = 9
# height = 222.51
# f_string = f'Имя: {name}, возраст: {age} лет, рост: {height}'
#
#
# print(f_string)















# min_val = 5
# max_val = 50
#
# nm_string = 'Введите целое число от %d до %d' % (min_val, min_val)
#
# print(nm_string)





# name = 'Виктор'
# age = 9
# height = 222.51
#
# f_string = '%9s, \nвозраст: %2d лет, \nрост: %6.1f см.' % (name, age, height)
# print(f_string)












#  #placeholder
#  # %d - число  %10d число из 10 знаков
#  # %s - строка
#  # %f - float
#
#
# name = 'Виктор'
# age = 9
# height = 222.51
#
# f_string = '%9s, \nвозраст: %2d лет, \nрост: %6.1f см.' % (name, age, height)
# print(f_string)
#












# lst = [5, 1, 3, 2, 4]
# lst.sort()
# #   Если так написать print(lst.sort()) то он вернет ничего так как он просто сортирует и не возвращает
# print(lst)
# print(sorted(lst))  #а вот сортед возвращает



# string = 'тиливизор'
#
# norm_string = string.replace('и','е', 2)
#
# print(norm_string)
#
# print(string.replace('и','е', 2))





# phone = '+7-012-345-67-89'
#
#
# print('Исходная строка:', phone)
#
# spaced_phone = phone.replace('-', ' ')
#
# print('Телефон через пробел:', spaced_phone)
#
# temp = phone.replace('-', ' (', 1) #ищи такой символ с начала и замени
# print(temp)
#
# bracked_code = temp.replace('-', ') ', 1)
# print(bracked_code)










# string = 'Видеть, вертеть, смотреть'
#
# #find(что, старт, стоп)
# index = string.find('еть')
# print(index)  #3 (начиная с нуля)
#
# index = string.find('еть', 10)
# print(index)  #12 (начиная с нуля или начала строки)
#
# index = string.find('еть', 15, 20)
# print(index)  #-1 (т.е. не найдена)



















# t = 20
#
# print('тепло') if t >= 20 else print ('прохладно')
























# #определяем количество букв в слове
#
# source = 'город рим'
#
# d = dict()
# source = ''.join(source.split())
#
# for letter in source:
#     if letter in d:
#         d[letter] += 1
#     else:
#         d[letter] =  1
#
# for k, v in d.items():
#     print(k, v , sep='-')





# #перевернули слово
#
# source = 'город рим' #миргород
#
# lst = source.split() #разделяем строку чтобы провернуть манипуляции
#
#
# print(lst[0][::-1] +' '+ lst[0] +' '+ lst[1][::-1]+lst[0])



















# abc = 'АБВГДЕЖЗ'
#
# text = input('')
# for letter in text:
#      if letter in abc:
#          abc[(index + 3) % 33]  #забираем текст с конца через остаток




















# from random import randint
#
# num = randint(1, 10)
#
# choice = int(input('Введите число: '))
# while choice != num:
#     if choice < num:
#         print('Ваше число меньше загаданного')
#     else:
#         print( 'Ваше число больше загаданного')
#     choice = int(input('Введите число: '))
# print('Ура, Вы угадали. Это именно', num)



#Regular Expressions (pattern)

import re

pattern = r'\b\w{3}\b' #найдём все слова из 4 букв
test_string = 'мама мыла раму, а папа был на пилораме'

result = re.findall(pattern, test_string)

print(result)








# import re
#
# pattern = '20'
# test_string = '10 плюс 20 будет 30'
#
# result = re.search(pattern, test_string)
#
# print(result.span())
























#Syntax Sugar



# strings = ['Арбуз', 'Виноград', 'Банан']
# s_list = sorted(strings)
#
# print(s_list)









# import math
# num_list = [1,2,3,4,5]
# #def doubled(x):
# #    return x * 2
# # lambda <аргумент(ы)>: <выражение с этими аргументами>
#
#
# double_list = list(map(lambda x: math.pow(x,3),num_list)) #2,4,6,8,10
# print(double_list)





# num_list = [1,2,3,4,5]
# #def doubled(x):
# #    return x * 2
# # lambda <аргумент(ы)>: <выражение с этими аргументами>
#
#
# double_list = list(map(lambda x:x *2,num_list)) #2,4,6,8,10
# print(double_list)



# num_list = [1,2,3,4,5]
# #def doubled(x):
# #    return x * 2
# # lambda <аргумент(ы)>: <выражение с этими аргументами>
# doubled = lambda x:x *2
#
# double_list = list(map(doubled,num_list)) #2,4,6,8,10
# print(double_list)











# num_list = [1,2,3,4,5]
# def doubled(x):
#     return x * 2
# double_list = list(map(doubled,num_list)) #2,4,6,8,10
# print(double_list)











# num_list = [1,2,3,4,5]
# str_list = list(map(str,num_list))
#
# print(str_list)
# # print(''.join())  #12345







#функцию можно предавать в другую функцию как объект

# люся = print
# люся('helo')
















# def average(*args):
#     summ = sum(args)
#     num = len(args)
#
#     print(f'Среднее арифметическое будет {sum(args) / len(args)}. ')
#
#
# average(1,2,3,4,5)





















# #упрощенная версия
#
# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#
#     try:
#         print(int(a)/int(b))
#         break
#     except ZeroDivisionError:
#             print('На ноль делить нельзя!')
#     except ValueError:
#         print('необходимо вводить только числа.')






#
# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#
#
#     if a.isdigit() and b.isdigit():  #Строки a и b - числа?
#         if int(b) == 0: #если второе число равно нулю
#             print('На ноль делить нельзя!')
#         else:
#             print(int(a)/int(b))
#             break
#     else:
#         print('необходимо вводить только числа.')





















# #PicklingError - проблемы с сериализацией
# #UnpicklingError - проблемы с десериализацией объекта (структуры)
#
#
# min_val = 1
# max_val = 10
# s_num = input(f'Введите целое число в диапазоне от {min_val} до {max_val}')
#
# try:
#     text = input('Введите текст: ')
#     assert len(text) > 3 #утверждение
# except AssertionError:
#     print('Длина текста меньше 3-х символов')



class Fruit:
    pass

a = Fruit()
b = Fruit()

print(type(a))























#декораторы функций

def benchmark(func):
    import time
    def wrapper():
        start=time.time()
        func()
        end=time.time()

        print(f'Затраченное время: {end - start} сек.')
    return wrapper



@benchmark
def long_list_creator():
     a=[i for i in range(1000000)]

long_list_creator()




















# def wrapper():
#    def say_hello():
#       print('Hello')
#    say_hello()
#
# def higher_order(func):
#     func() #Вызов  функции, переданной в качестве параметра
#
# def decorator_function(func):
#    def wrapper():
#        print(f'Оборачиваемая функция: {func}')
#        print(f'Выполняем обёрнутую функцию')
#        func()
#        print('Выходим из обёртки')
#    return wrapper
#
#
# @decorator_function
# def say_hello():
#     print('Hello')
#
#
# say_hello()




# def wrapper():
#    def say_hello():
#       print('Hello')
#    say_hello()
#
# def higher_order(func):
#     func() #Вызов  функции, переданной в качестве параметра










# import re
#
# pattern = '<img[^>]+src="([^">]+)"' #пишем без пробелов
# test_string = 'Картинка <img src="bg.jpg"> тексте </p>'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result)













# import re
#
# pattern = 'стеклянн?ый' #пишем без пробелов
# test_string = 'стекляный, стеклянный, оловянный, деревянный'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result)








# #? - аналог {0,1}
# # * аналог от 0 до бесконечности
# # + аналог 1 до бесконечности
#
#
# import re
#
# pattern = r'\+7\d{10}' #пишем без пробелов
# test_string = 'Google: +78121234567'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result)

















# import re
#
# pattern = r'Go{2,}gle' #пишем без пробелов
# test_string = 'Google, Gooogle, Gooooooogle'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result)












# # а  привичка записывать - точным.
# # {m} - ровно m раз
# # {n,m} - не более m раз
# import re
#
# pattern = r'o{2,5}' #пишем без пробелов
# test_string = 'Google, Gooogle, Gooooooogle'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result)







# # а  привичка записывать - точным.
# # {m} - ровно m раз
# # {n,m} - не более m раз
# import re
#
# pattern = r'\((.+?)\)' #выудить то, что в скобках
# test_string = 'Поиск по образцу (pattern)!'
#
# result = re.findall(pattern, test_string) #игнорируем регистр
# print(*result, sep='')













# import re
#
# pattern = '[^абвгд]' #от 00 до 59
# test_string = 'АБВГДейка - детская передача!'
#
# result = re.findall(pattern, test_tring, re.I) #игнорируем регистр
# print(*result, sep='')
















# import re
#
# pattern = '[0-5][0-9]' #от 00 до 59
# test_string = 'Время - 07:45!'
#
# result = re.findall(pattern, test_string) #сгруппировать
# print(result)
#
# # if result:
# #      print(result[0], result.span())
# # else:
# #     print('Нету')











# import re
#
# pattern = '[0-5][0-9]'
# test_tring = 'Время - 07:45!'
#
# result = re.search(pattern, test_tring)
#
# if result:
#      print(result[0], result.span())
# else:
#     print('Нету')





# import re
#
# pattern = r'начало!\Z' #заканчивается ли на это строка
# test_tring = 'Главное - начало!'
#
# result = re.search(pattern, test_tring)
#
# if result:
#      print(result[0], result.span())
# else:
#     print('Нету')


















# import re
#
# pattern = r'\d{3}' #найдём трехзначные цифры
# test_tring = 'для экстренных вызовов 112'
#
# result = re.search(pattern, test_tring)
#
#
# print('Цифры есть') if result else print ('Цифр нет')
# print(result[0], result.span())














# import re
#
# pattern = r'\d' #найдём все цифры в строке текста от 0 до 9
# test_tring = 'для экстренных вызовов 112'
#
# result = re.search(pattern, test_tring)
#
#
# print('Цифры есть') if result else print ('Цифр нет')






# rus = ['стул', 'стол', 'яблоко']
#
# eng = ['chair', 'table', 'apple']
#
# d = dict(zip(rus, eng))
#
# print(d)









# import math
#
# lst = [1, 2, 3, 4, 5]
#
# power = lambda x, y: math.pow(x, y)
#
# res = list(map(lambda x: power(x, 2), lst))
#
# print(*res)













# import re
#
# pattern = r'\b\w{2}\b'
# test_tring = 'мама мыла раму, а папа был на пилораме'
#
# result = re.findall(pattern, test_tring)
#
# print(result)
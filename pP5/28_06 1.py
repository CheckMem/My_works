

























# # Throw Exception
# # Raise Exeption
#
# min_val = 1
# max_val = 10
# s_num = input(f'Введите целое число в диапазоне от {min_val} до {max_val}')
#
# try:
#      num = int(s_num)
#      if not min_val <= num <= max_val:
#         raise ValueError('введенное число вне заданного диапазона')
# except ValueError as exp:
#   print(f'Вас просили ввести целое число, а Вы ввели "{s_num}"')
#   print('будьте внимательней', exp)























# #Задача организовать вечный цикл продолжаемый до тех пор
# #пока не будет введено целое число
#
# flag = False
#
# while True:
#     try:
#         num = int(input('Введите целое число: '))
#     except ValueError:
#         print(f'некорректный ввод')
#     else:
#         flag = True
#         print(f'Вы ввели {num} и это верно! До свидания!')
#         break
#     finally:
#        if flag:
#         print('hasta la vista')






















# try:
#     f = open('informer.txt')  #пробуем открыть
#     print(f.read())
#     is_opened = True # устанавливаем флаг открытия
#
#
#
# except FileNotFoundError:
#     print('Файл не существует')
#     is_opened = False #файл и не открывался (флаг обнуляем)
# finally:
#     if is_opened:   #если файл был успешно открыт на чтение
#         print('Файл прочитан и закрыт.')
#         f.close()
#     else:
#         print('Файл и не открывался, закрывать нечего!')






















# print('Делим 10 на любое целое число')
#
# try:
#      value = int(input(' На что делим 10:(введите целое число) '))
#      res = 10/ value
#      print(f'Остаток от деления {value} на 10 будет {res}.')
#
# #EOF - End of File
#
#
# except ValueError:
#     print('Вас просили ввести целое число. А вы!!!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except Exception as exp:
#     print('Вот что произошло->', exp, exp.__class__.__name__)
#
# finally:
#     print('Всё относительно!')  #выполняется в любом случае






















# print('Делим 10 на любое целое число')
#
# try:
#      value = int(input(' На что делим 10:(введите целое число) '))
#      res = 10/ value
#      temp = value+ 'Привет'
#      print(f'Остаток от деления {value} на 10 будет {res}.')
#
#
#
# except ValueError:
#     print('Вас просили ввести целое число. А вы!!!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except Exception as exp:
#     print('Вот что произошло->', exp, exp.__class__.__name__)






# print('Делим 10 на любое целое число')
#
# try:
#      value = int(input(' На что делим 10:(введите целое число) '))
#      res = 10/ value
#      print(f'Остаток от деления {value} на 10 будет {res}.')
# except ValueError:
#     print('Вас просили ввести целое число. А вы!!!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')








# дробное выдаёт ошибку

# print('Считаем остаток от деления на 10!')
#
# value = int(input(' От чего считаем остаток от деления: '))
# res = value % 10
# print(f'Остаток от деления {value} на 10 будет {res}.')



















# try:
#     f = open('text.txt')
#     ############
#     f.close()
#     print('Всё в порядке')
# except FileNotFoundError:
#     f =open('text.txt', 'w')
#     ############
#     f.close()
#     print('Файл был удален')
#     print('И он был создан заново')















# #Исключения - Exception
#
# name = input('Введите своё имя')
#
# try:
#     print(nname)
# except NameError:
#     name = input('Ваше имя: ')
#     print('Вас зовут', name)






















#тоже хуй знает

# d = dict()
#
# with open('dictionary.bin', 'wt', encoding='utf-8') as f:
#     keys = f.readline()
#     values = f.readline()
#
#
# key_list = keys.split()
# value_list = values.split()
# lenght = len(key_list)
#
# for i in range(lenght):
#     d[key_list[i]] = value_list[i]
#
#
# print(d)




















# d = {
#      'стол': 'table',
#      'стул': 'chair',
#      'яблоко': 'apple',
#      'автобус': 'bus'
#      }
#
# keys = tuple(d.keys())
# values = tuple(d.values())
#
# with open('dictionary.bin', 'wt', encoding='utf-8') as f:
#     print(*keys, file = f)
#     print(*values, file = f)
















# #программа которая нихуя не работает и вроде должна записывать слова в словарь
#
# import pickle  #pickling - засолка, консервация данных, сериализация или десериализация
#
#
# # fname = 'info.txt'
# with open('dictionary.bin', 'rb') as f:
#      d = pickle.load(f)
#
#
# while True:
#
#       word = input('введите слово для перевода (или QQ - для выхода): ')
#       if word =='QQ':
#           break
#
# if word in d:
#     print(f'Слово {word} переводится как {d[word]}.')
# else:
#     print('Я не знаю, но можете мне подсказать')
#     new_word = input(f'Как переводится {word}: ')
#     d[word] = new_word
#
# with open ('dictionary.bin', 'wb') as f:
#     pickle.dump(d, f)
#     # d = pickle.load(file)
#
#
# # print (d)

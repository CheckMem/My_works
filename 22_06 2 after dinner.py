
string = 'аргентина манит негра'

new_string = ''.join(string.split())
print(new_string)





















# string = '        Python Language       '
#
# string = string.strip()
# print(string)
#
# lst = string.split()
#
# lst[0] = 'Java'
# new_string = ' '.join(lst)
# print(new_string)
#
# b_list = ['Аптека','Улица','Фонарь']
#
# b_string = ', '.join(b_list).capitalize()
# print(b_string)
#
#
# b_string = ', '.join(b_list)
# print(b_string.capitalize())












# string = '        Python Language       '
#
# string = string.strip()
# print(string)
#
# lst = string.split()
#
# lst[0] = 'Java'
# new_string = ' '.join(lst)
# print(new_string)






# print(string.capitalize())
#
# print(string.title())
#
# print(string.upper())
#
# print(string.lower())
#
# print(num.isnumeric())
#
# print(string.isdigit())

















# code = 176
#
# print(25,chr(code),'C')
#
# print(25,'\u2710' + 'C')



# symbol = 'F'
# code = ord(symbol)
# print(code)











# l = ['a','b','c']
#
# print('Вот ABC первые 3 буквы: ')
#
# for i, v  in enumerate(l):
#     print('\t',i+1, v)





























# trains = {
#     '001A': ['"Красная стрела"', 'СПб-Москва']
# }







# if 'а' in 'собака':
#     print('Есть такая буква')





















# d = {
#     'Дмитриев': 'Скульптор',
#     'Иванов':  'Программист',
#     'Петров':  'Художник',
#     'Сидоров': 'Стоматолог',
# }
#
# d['Никитин'] = 'Сисадмин'
#
# if 'Стоматолог' in d.values():
#         print('Он есть')
# if 'Петроа' in d.keys():
#         print('Он есть')














# d = {
#     'Дмитриев': 'Скульптор',
#     'Иванов':  'Программист',
#     'Петров':  'Художник',
#     'Сидоров': 'Стоматолог',
# }
#
# d['Никитин'] = 'Сисадмин'
#
# for item in d.values():
#     print(item)
#
# for item in d.keys():
#     print(item)
#
# for k, v in d.items():
#     print(k, '->', v)
































# Словарь

# d = {
#     'Дмитриев': ['Плотник','Скульптор'],
#     'Иванов':  'Программист',
#     'Петров':  'Художник',
#     'Сидоров': 'Стоматолог',
# }
#
# d['Никитин'] = 'Сисадмин'
#
# for item in d:
#     if isinstance(d[item], list):
#          print(item + ':', d[item][1])
#     else:
#         print(item + ':', d[item])
#

















# lst = {2, 3, 5, 7, 11}
# for index, value in enumerate(lst):
#     print('Индекс:', index, 'Значение:', value)
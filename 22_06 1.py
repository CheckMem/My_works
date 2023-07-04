string = 'телевидение'

st = set (string)
print (*st, sep='')

#множества


a = {1,2,3,4}
b = {2,3,5,7,11}

#объединение

print(a.union(b))#убрал двойку

#пересечение

print(a.intersection(b)) #оставил только повторы

#разность
print(a.difference(b)) #элементы входящие в а, но не входящие в b

#симметричная разность

print(a.symmetric_difference(b))














# a = list()
# b = tuple()
# c = {'a','b','c','a'}
#
# print(c) #множество убивает повторную "a" поэтому полезна в прогах без повторов

















# x, y = input('ВВедите x: '), input('ВВедите y: ')
#
# print(x, y)

































#вывод правда ли
#print(isinstance(3, int))

























# def swap(a):
#      x = a ** 2
#      y = 2 * a
#      z = a / a
#      return x,y,z
# temp = swap(8)










# def swap(a, b):
#     b, a = a, b
#     return a, b
#
# print(*swap(1, 2))


















# l = ['пришла', 'весна']
#
# l[1], l[0] = l[0], l[1]
#
# print(*l)






# l = ['пришла', 'весна']
#
# a, b = 3, 4
# b, a = a, b #swap
#
# print(a,b)













#как присвоить без 3 переменной

# l = ['пришла', 'весна']
#
# a = 3
# b = 4
#
# temp = a
# a = b
# b = temp
#
# print(a,b)










# a = (1,1)
#
# print(type(a))
































# import random as r
# r_string = 'qwertyuiopasdfghjklQWERTYUIOPASDFGHJKL0123456789~'
# lst = list(r_string)
#
# r.shuffle(lst)
#
# temp = lst[:8]
# if '~' in temp:
#     print(*temp, sep='')
#
#
# else:
#     temp.append('~')
#     print(*temp, sep='')





















# import random as r
#
#
# r_string = 'qwertyuiopasdfghjklQWERTYUIOPASDFGHJKL0123456789~'
#
# lst = list(r_string)
#
# r.shuffle(lst)
# print(lst)










# import random as r
#
#
# r_string = 'qwertyuiopasdfghjklQWERTYUIOPASDFGHJKL0123456789~'
#
# lst = list(r_string)
#
# new_list = r.shuffle(lst)
# print(lst)
#






















# import random as r
# colors = ['red','green','blue', 'yellow','orange', 'purple']
#
# lst = list('Python')
# print(lst)











# import random as r
# colors = ['red','green','blue', 'yellow','orange', 'purple']
#
# value = r.choice(colors)
#
# print(value)
# print(colors[index])
#
# for _ in range(10):
#     index = r.randint(0, len(colors))
#     print(index)



















# import random as r
# colors = ['red','green','blue', 'yellow','orange', 'purple'
#
# print(colors[index])
#
# for _ in range(10):
#     index = r.randint(0, len(colors))
#     print(index)
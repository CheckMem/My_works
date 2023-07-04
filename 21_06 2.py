
def greeting(hour):
    pass
    if  8 <= hour < 12:
        print('доброе утро')
    elif hour >= 12 and hour < 18:
        print('добрый день')
    elif hour >= 18 and hour < 22:
        print('добрый вечер')
    else:
        print('доброй ночи')

steps_yast = 5500 # шаги за вчера
steps_today = 5000 # шаги за сегодня
str_out = 'Вы прошли '


steps_sum = steps_yast + steps_today # сумма шагов

if steps_sum >= 10000:
    str_out += str(steps_sum) + ' шагов. Поздравляем!'
    str_out += '\n Вам стал доступен' + str(gyges) + 'Гб.'
    str_out += '\n До следующего Гб Вам осталось пройти '
    str_out +=str(10000* gyges - (steps_sum - 10000))
    str_out += 'шагов.'
    pass
else:
    str_out += 'пока что только '
    str_out += str(steps_sum)
    str_out += 'шагов. Есть к чему стремиться'
    str_out += '\nДля получения 1Гб Вам нужно пройти ещё'
    str_out += str(10000-steps_sum) + 'шагов.'
print(str_out)

























# # c 8 до 12 доброе утро
# # с 12 до 18 добрый день
# # с 18 до 22 добрый вечер
# # во всех остальных случаях - доброй ночи
#
# def greeting(hour):
#     pass
#     if  8 <= hour < 12:
#         print('доброе утро')
#     elif hour >= 12 and hour < 18:
#         print('добрый день')
#     elif hour >= 18 and hour < 22:
#         print('добрый вечер')
#     else:
#         print('доброй ночи')
#
# for h in range (24):
#     print('На часах', h, end=': ')
#     greeting(h)













# def divider(a, b):
#     if b != 0:
#        return a / b
#     return 'Ошибка деления на ноль'
#
# def factorial1(n):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x
# def factorial_r(n):
#     if n == 0:
#         return 1
#     return n * factorial_r(n-1)
# print (factorial1(5))
# print (factorial_r(3))



# def divider(a, b):
#     if b != 0:
#        return a / b
#     return 'Ошибка деления на ноль'
#
# def factorial(n):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x
# print (factorial (5))




# def divider(a, b):
#     if b != 0:
#        return a / b
#     return 'Ошибка деления на ноль'
# a = 3
# b = 0
#
# print(divider(a, b))









# def divider(a, b):
#     if b != 0:
#        return a / b
#
# a = 3
# b = 0
#
# print(divider(a, b))
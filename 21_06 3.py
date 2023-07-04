number = input ('Введите целое число:')

a = 0
for i in number:
    a += int(i)

print('Сумма разрядов числа', number, '=', a)










# string = input('Введите строку: ')
#
# if string == string[::-1]:
#     print(string, '-палиндром')
# else:
#     print(string, 'не палиндром')










# colors = ['red','green','blue', 'yellow','orange', 'purple']
#
# print(colors[1:6:2])
#
# print(colors[::-1])
# string = 'python'
# print(string[::-1])

















# import turtle as t
#
# colors = ['red','green','blue', 'yellow','orange', 'purple']
# angle = 60
#
# t.speed(0)
# t.bgcolor('black')
#
# for x in range(201):
#     t.pencolor(colors[x % 6])
#     t.width(x // 10 + 1)
#     t.forward(x)
#     t.left(angle)
# t.mainloop()
#
#
#
#


















# from datetime import datetime
#
# get_time = datetime.time(datetime.now())
# cur_time = get_time.strftime("%H:%M")
# hour = int(get_time.strftime("%H"))
# print('На часах', cur_time)
# def greeting(hour):
#     pass
#     if  8 <= hour < 12:
#         return'доброе утро'
#     elif hour >= 12 and hour < 18:
#         return'добрый день'
#     elif hour >= 18 and hour < 22:
#         return'добрый вечер'
#     else:
#         return'доброй ночи'
#
# print(greeting(hour))
#
# color = input('Цвет шарика: ')
# if color == 'зелёный' or color == 'синий':
#     print('Эти шары подходят')
# else:
#     print('Не годится')
#








# from datetime import datetime
#
# get_time = datetime.time(datetime.now())
# cur_time = get_time.strftime("%H:%M")
# returncur_time)























# def greeting(hour):
#     pass
#     if  8 <= hour < 12:
#         return'доброе утро')
#     elif hour >= 12 and hour < 18:
#         return'добрый день')
#     elif hour >= 18 and hour < 22:
#         return'добрый вечер')
#     else:
#         return'доброй ночи')
#
# steps_yast = 35500 # шаги за вчера
# steps_today = 5000 # шаги за сегодня
# str_out = 'Вы прошли '
#
#
# steps_sum = steps_yast + steps_today # сумма шагов
#
# if steps_sum >= 10000:
#
#     gyges = steps_sum //10000
#     str_out += str(steps_sum) + ' шагов. Поздравляем!'
#     str_out += '\n Вам стал доступен' + str(gyges) + ' Гб.'
#     str_out += '\n До следующего Гб Вам осталось пройти  '
#     str_out +=str(10000* gyges - (steps_sum - 10000))
#     str_out += ' шагов.'
#     pass
# else:
#     str_out += 'пока что только '
#     str_out += str(steps_sum)
#     str_out += 'шагов. Есть к чему стремиться'
#     str_out += '\nДля получения 1Гб Вам нужно пройти ещё'
#     str_out += str(10000-steps_sum) + 'шагов.'
# returnstr_out)
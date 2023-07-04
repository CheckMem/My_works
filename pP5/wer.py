
# import tkinter as Tk
# from tkinter import *
# from tkinter import messagebox
#
#
# window = Tk() #Создаём окно приложения.
# window.title("Калькулятор индекса массы тела (ИМТ)") #Добавляем название приложения.окно открылось и сразу закрылось
#
# window.mainloop() #чтобы окно не закрывалось пока пользователь не захочет, но размер окна бесформенный и там
# # не видно название окна
#
# frame = Frame(
#    window, #Обязательный параметр, который указывает окно для размещения Frame.
#    padx = 10, #Задаём отступ по горизонтали.
#    pady = 10 #Задаём отступ по вертикали.
# )
# frame.pack(expand=True) #Не забываем позиционировать виджет в окне.
# # Здесь используется метод pack. С помощью свойства expand=True указываем,
# # что Frame заполняет весь контейнер, созданный для него.


from tkinter import *
from tkinter import messagebox


def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get()) / 100
   bmi = kg / (m * m)
   bmi = round(bmi, 1)

   if bmi < 18.5:
      messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
   elif (bmi > 18.5) and (bmi < 24.9):
      messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
   elif (bmi > 24.9) and (bmi < 29.9):
      messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
   else:
      messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')


window = Tk()
window.title('Калькулятор индекса массы тела (ИМТ)')
window.geometry('400x300')

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

height_lb = Label(
   frame,
   text="Введите свой рост (в см)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
   frame,
   text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
   frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
   frame,
   text='Рассчитать ИМТ',
   command=calculate_bmi
)
cal_btn.grid(row=20, column=2)

window.mainloop()
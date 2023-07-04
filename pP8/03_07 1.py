
from tkinter import * # GUI - Graphics User Interface
from PIL import ImageTk, Image
from tkinter import filedialog









status = False
def rgb(r=0, g=0 ,b=0):
    return f'#{r:02x}{g:02x}{b:02x}' # x - последняя буква hex

# from lib import Okno
#
# if __name__ =='__main__':
#   app = Okno()
class Okno:
    def __init__(self):
        self.window = Tk()
        self.window.title('Добро пожаловать в Tkinter')
        self.window.geometry('800x600')
        self.window.resizable(False, False)

        self.lbl = Label(self.window, text='Картинка ниже')
        self.lbl.pack()
        self.canvas = Canvas(self.window, height=100, width=100)
        self.image = ImageTk.PhotoImage(Image.open("image1.png"))
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        self.canvas.pack()
        # lbl = Label(self.window, text = 'Это Ярлык или Метка')
        # lbl.pack()

        self.btn = Button(self.window, text='Нажми', command= self.click)
        self.btn.pack()

        self.window.mainloop()

    def click(self):
        path = filedialog.askopenfilename()
        original = Image.open(path)
        w,h = original.size
        ratio = w/h
        if w>133:
            original.resize((133, int(133*ratio)))
        self.image = ImageTk.PhotoImage(Image.open("zmei.png"))
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
#
#
# app = Okno()
# #
# def click():
#     global status
#     if not status:
#         lbl['text'] = 'Кнопка нажата'
#         lbl['background'] = rgb(255,0 , 0)
#         btn['text'] = 'Меня нажали'
#         btn['background'] = rgb(255, 0, 0)
#     else:
#
#         lbl['text'] = 'Кнопка нажата'
#         lbl['background']=self.window.cget('bg')
#         btn['text'] = 'Меня нажали'
#         btn['background'] =self.window.cget('bg')
#     status = not status #инверсия


# self.window.mainloop()































# from lib import Rectangle
#
# rect1 = Rectangle(10,20)
# rect2 = Rectangle(10,20)
#
# print(rect1 != rect2)
#
# print(rect1 > rect2)










# from lib import Time
#
# t = Time (45, 27)
#
# print(t.info())
#
# t1 = Time(10,40)
# t2 = Time(10,19)
#
# t3=t2+t1  #t1.__add__(t2)
# print(t3.info()) #str->

# from lib import Special
#
# s = Special()
#
# print(s + 1)
# print(1 + s)
# s +=1
# print(s)













# from lib import List
#
# l = List('5')
#
# l.show_list()
#
# l.clear()
#
# l.show_list()

















# from lib import Car
#
# a = Car()
# b = Car()
# c = Car()
# c.count
# print(Car)
#
# b.start_engine()
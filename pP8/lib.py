from math import pi
def get_size(obj):
    print(f'Размер: {obj.__sizeof__()} байт(a)')
# комментарий

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
        self.canvas = Canvas(self.window, height=100, width=100)
        self.image = ImageTk.PhotoImage(Image.open("zmei.png"))
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)


app = Okno()

class Rectangle:
    def __init__(self,one_side, another_side):
        self.one_side = one_side
        self.another_side = another_side
        self.name = 'Прямоугольник'


    def area(self):
       return self.one_side * self.another_side

    def perimeter(self):
        return self.one_side*2 + self.another_side*2

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False


    def __ne__(self, other):
        print('Меня вызвали')

    def __lt__(self, other):
        print('Вызван "меньше чем"')

    def __ge__(self, other):
        print('Вызван "меньше чем"')
















class Time:
    def __init__(self, minutes, seconds):
         self.minutes = minutes
         self.seconds = seconds
    def __str__(self):
        return f'{self.minutes:02d}:{self.seconds:02d}'

    # def report
    #     return f'{self.minutes:02d}:{self.seconds:02d}'
    def info(self):
        return f'{self.minutes:02d}:{self.seconds:02d}'


    def __add__(self, other):

        m = self.minutes + other.minutes
        s = self.seconds + other.seconds

        m += s //60
        s = s % 60
        return Time(m,s)














class Special:
    def __init__(self):
        self.value = 10
    def __add__(self, other):
        return 'Выполнился __add__'
    def __radd__(self, other):
        return 'Выполнился __radd__'
    def __iadd__(self, other):
        self.value += other
        return 'Выполнился __iadd__'
    def __str__(self):
        return f'Значение {self.value}'













class List:
    def __init__(self, n=0):
        if n ==0:
            self.a =[]
        else:
          try:
            n = int(n)
            n = abs(n)
            self.a = [0 for i in range(n)]
          except ValueError:
              self.a = []

    def add(self, value=''):
        self.a.append(value)
    def clear(self):
        self.a.clear()
    def remove(self, value):
        try:
            self.remove(value)
        except:
            print('Элемента нет в списке')
    def show_list(self):
          print(*self.a, sep=', ')









class Car:
    count = 1 #статический атрибут
    def __init__(self):
        self.engine_on = False  #пока не заведён
    def start_engine(self):
        self.engine_on = True #завели
        Car.count +=1 #увеличиваем на 1
    def drive(self, place):
        if self.engine_on:
            print(f'Едем на {place}')
        else:
            print('Забыл завести мотор!')
@staticmethod
def get_count():
     return Car.count


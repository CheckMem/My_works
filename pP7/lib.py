from math import pi
def get_size(obj):
    print(f'Размер: {obj.__sizeof__()} байт(a)')

#isinstance

# def isinstance(figure, int | str)


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

    def add (self, value =''):
        self.a.append(value)
    def clear(self):
        self.a.clear()
    def remove (self, value):
        try:
               self.remove(value)
        except:
            print('Элемента нет в списке')









def print_figure_info(figure):
    # if isinstance(figure, Square):


    # if figure.name == 'Квадрат':
    #     print('Для квадрата:\n')
    #
    # elif figure.name == 'Прямоугольник':
    #     print('Для прямоугольника:\n')
    # else:
    #     print('Для круга:')
    # print(type(figure).__name__)
    print(f'Area={figure.area()}\nPerimeter={figure.perimeter()}')





# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.x = side1
#         self.y = side2
#         self.z = side3
#
#     class EquilateralTriangle(Triangle):
#         def __init__(self, side):
#             Triangle.__init__(self, side, side, side)
#
#             Triangle.a = side
#             Triangle.b = side
#             Triangle.c = side
#     def area(self):
#         return self.x * self.y * self.z
#     def perimeter(self):
#         return self.x + self.y + self.z


#
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#        return pi * self.radius **2
#
#     def perimeter(self):
#         return 2 * pi * self.radius
#
# class Square(Rectangle):
#     def __int__(self, side):
#         super().__init__(side,side)
#
#         self.side = side
#         self.name = 'Квадрат'



    # def area(self):
    #     return self.side**2
    #
    # def perimeter(self):
    #     return self.side*4


class Rectangle:
    def __init__(self,one_side, another_side):
        self.one_side = one_side
        self.another_side = another_side
        self.name = 'Прямоугольник'


    def area(self):
       return self.one_side * self.another_side

    def perimeter(self):
        return self.one_side*2 + self.another_side*2









class Book:
    def __init__(self, name, author):
        self.name =  name
        self.author = author

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author







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



class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def set_color(self, new_color): #setter
        self.color = new_color

    def get_color(self):  #getter
        return self.color

    def get_info(self):  #getter
        print(f'{self.name }')







class Greeter:
    def say_hello(self):
        print('Hello')

    def hello_name(self,name):
        print(f'Hello,{name}')

    def hello_and_talk(self, name, weather):
        print(f'Hello, {name}')
        print(f'{name},{weather}')

















# class Fruit:
#     pass
#
# class Greeter:
#     def say_hello(self):
#         print('Hello')
#
#     def hello_name(self,name):
#         print(f'Hello,{name}')
#
#     def hello_and_talk(self, name, weather):
#         print(f'Hello, {name}')
#         print(f'{name},{weather}')
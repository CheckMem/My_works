
from PIL import Image
from PIL import ImageDraw


BLACK = (0,0,0)
YELLOW = (255,255,0)
W, H = (100, 100)


canvas = Image.new("RGB", (W, H), BLACK) #создали холст
draw = ImageDraw.Draw(canvas)

draw.line((W,0,0,H),fill=YELLOW, width=1)



canvas.save('image.png', 'PNG')

canvas.show()











# #МОДУЛИ
#
#
# from lib import *
#
# def main():
#     say_hellot('Tom')
#     div(2, 3)
#
# if __name__ == '__main__':
#      main()












# from lib import div, say_hello
# say_hello('Tom')
#
# div(2, 0)
#
# print(__name__)

# import lib
# lib.say_hello('Tom')
#
# lib.div(2, 0)










































# n = '5 6 7 9'
# a= sum([int(x) for x in n.split()])
# print(a)









# a = '5 6 7 9'
#
# s = ''. join(a.split())
#
# summ = 0
#
# for x in s:
#     summ += int(x)
#
# print(summ)
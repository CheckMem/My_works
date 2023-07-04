from PIL import Image, ImageFilter, ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont


#блок констант
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE= (255,255,255)
W, H = (200, 200) #можно бeз скобок
RW = 50
RH = 50

original = Image.open('../pP8/python1.png')
W,H = original.size
ratio = W/H #пропорция


original = original.convert('RGB')
blur = original.filter(ImageFilter.BLUR)
blur.save('puthon_blur.png')


blourbox = original.filter(ImageFilter.BoxBlur(50))
blourbox.save('puthon_box.png')

blourgauss = original.filter(ImageFilter.GaussianBlur(5))
blourgauss.save('puthon_gauss.png')

contour = original.filter(ImageFilter.CONTOUR)
contour.save('countered.png')

# C:\Users\Student\AppData\Local\Programs\Python\Python39\Scripts\pip.exe

sharped = ImageEnhance.Sharpness(original)
sharped_image = sharped.enhance(10.0)
sharped_image.save('sharped.png')
# mode = original.mode
# print(mode)


































# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
#
# BLACK = (0,0,0)
# YELLOW = (255,255,0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# WHITE= (255,255,255)
# W, H = (200, 200) #можно бeз скобок
# RW = 50
# RH = 50
# TEXT = 'PYTHON'
# CELLS = 8
# W,H = CELLS * RW, CELLS * RH
#
# original = Image.open('python1.png')
#
# # print('Формат:',original.format)
# # print('Цветовая схема:', original.mode)
# # print('Размеры:', original.size)
# # W,H = CELLS * RW, CELLS * RH
# # print('Размеры:', W,'x',H)
# # required_height = 100 #обязательно хранить с высотой 100px
# # ratio = W / H
# # resized = original.resize((int(required_height * ratio), required_height))
# #
# # resized.save('image1.png', 'PNG')
#
# # cropped_image = original.crop(
# #
# #     (300,0,600,200)
# # )#обрезаем участок
# #
# # cropped_image.save('image1.png', 'PNG')
#
#
# pixels = original.load()
#
# # for x in range(W):
# #     for y in range(H):
# #         r,g,b = pixels[x,y]
# #         pixels[x,y] = g,b,r
# # original.save('inverted.png')
#
#
# for x in range(W//2):
#     for y in range(H):
#         r,g,b = pixels[x,y]
#         averaged = (r+g+b)//3
#         pixels[x, y] = pixels[W-x-1,y] = pixels[W-x-1,y], pixels[x, y]
# original.save('h_flipped.png')
# print(pixels)
#


















# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont


# #блок констант
# BLACK = (0,0,0)
# YELLOW = (255,255,0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# WHITE= (255,255,255)
# W, H = (200, 200) #можно бeз скобок
# RW = 50
# RH = 50
# TEXT = 'PYTHON'
# arial = 'C:\\Windows\\Fonts\\arial.ttf'
# CELLS = 8
# W,H = CELLS * RW, CELLS * RH
#
# canvas = Image.new("RGB", (W, H), BLACK) #создали холст
# draw = ImageDraw.Draw(canvas)
#
# for x in range(CELLS):
#     for y in range((x+1) %2, CELLS, 2):
#         draw.rectangle((x*RW, y*RW,
#                         (x+1)*RW-1,
#                         (y+1)*RW-1), fill = WHITE)
#
#
#
# canvas.save('image.png', 'PNG')
#
# canvas.show()



































#
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
#
#
# #блок констант
# BLACK = (0,0,0)
# YELLOW = (255,255,0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# WHITE= (255,255,255)
# W, H = (200, 200) #можно бeз скобок
# RW = 50
# RH = 50
# TEXT = 'PYTHON'
# arial = 'C:\\Windows\\Fonts\\arial.ttf'
#
#
#
# canvas = Image.new("RGB", (W, H), BLACK) #создали холст
# draw = ImageDraw.Draw(canvas)
#
# # font = ImageFont.truetype('arial.ttf', size=50)
# # draw.text((10, 10), TEXT, font=font)
# #
# # draw.ellipse((0, 150, 50, 200), fill=RED)
# # draw.ellipse((75, 75, 125, 125), fill=GREEN)
# # draw.ellipse((150, 0, 200, 50), fill=BLUE)
#
#
# # draw.polygon((W//2, 0, 0, H, W, H),
# #          fill=WHITE, outline = YELLOW)
#
#
# # draw.arc(xy=(25, 50, 175, 200), start=0, end = 270,
# #           fill=BLUE, width=10)
# # red (255, 0, 0)
# # draw.rectangle((0, 0, 50, 50), fill=RED)
# # draw.rectangle((75, 75, 125, 125), fill=GREEN)
# # draw.rectangle((W-RW, H-RH, W, H), fill=BLUE)
# #draw.line((W,0,0,H),fill=YELLOW, width=1)
#
#
#
# canvas.save('image.png', 'PNG')
#
# canvas.show()
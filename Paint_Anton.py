from tkinter import *
from random import *
from PIL import ImageTk, Image, ImageFilter

#создаём окно
root = Tk()
root.geometry('1000x800')
root.title('Paint and picture')

#список цветов
colors = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'grey', 'black']

# зарузка картинок
space = Image.open("space.jpg")
minecraft = Image.open("minecraft.jpg")
bit = Image.open("8_bit.jpg")
bit_city = Image.open("city-8bit.jpg")

#размер картинок
new_height = 730
new_width  = 780

#задаём размер картинок
space = space.resize((new_width, new_height), Image.ANTIALIAS)
bit = bit.resize((new_height, new_width), Image.ANTIALIAS)
minecraft=minecraft.resize((new_width, new_height), Image.ANTIALIAS)
bit_city=bit_city.resize((new_width, new_height), Image.ANTIALIAS)

#добявляем фильтр
space = space.filter(ImageFilter.CONTOUR)
bit = bit.filter(ImageFilter.CONTOUR)
minecraft = minecraft.filter(ImageFilter.CONTOUR)
bit_city=bit_city.filter(ImageFilter.CONTOUR)

#функция для Listbox, выбор картинки
def li(event):
    x = lis.curselection()
    num=lis.get(x)
    global image1
    if num == 'корабль':
        image = space
    elif num == 'дерево':
        image = bit
    elif num == 'город':
        image = bit_city
    elif num == 'минекрафт':
        image = minecraft
    image1 = ImageTk.PhotoImage(image)

#создаем listbox
lis=Listbox(width=30, height=7, bg='red', font='Times 18')
lis.grid(row=1, column=9, rowspan=3, sticky='news')
lis.bind("<<ListboxSelect>>", li)#связываем нажатие на Listbox и выполнение функции

#список Listbox
pictures = ['корабль', 'город', 'дерево', 'минекрафт']
#добавить в конец Listbox
for picture in pictures:
    lis.insert(END, picture)

#функция для рисования, выбор цвета в который окрашенна кнопка
def ButtonClick(event):
    global color
    t = event.widget
    color = t['bg'] #

#цикл создание 8 кнопок
for i in range(8):
    color = colors[i]
    btn = Button(root, width = '9', bg = color)
    btn.grid(row = 0, column = i)
    btn.bind('<Button-1>', ButtonClick) #связать левая кнопка мыши и функцию для рисования
#создаём ластик
car = Button(width = '9', bg = 'white', text = 'ластик')
car.grid(row=1, column=2)
car.bind('<Button-1>', ButtonClick)#связать левая кнопка мыши и функцию для рисования

# создаём поле введения толщины линии
entry = Entry(root, width = '10', bg = 'white')
entry.grid(row = 1, column = 0)

#функция толщины линии, устанавливает толщину линии
def SubmitClick(event):
    global t
    t = int(entry.get())
#кнопка толщина линии
submit = Button(root, width = '10', bg = 'white', text = 'толщина')
submit.grid(row = 1, column = 1)
submit.bind('<Button-1>',SubmitClick) #связать левая кнопка мыши и функции толщины линии

#функция для кнопки очистить
def ClearClick(event):
    picture.delete('all') #всю картинку удалить!

#кнопка очистить
clear = Button(root, width = '9', bg = 'white', text = 'очистить')
clear.grid(row = 1, column = 3)
clear.bind('<Button-1>',ClearClick)#связать левая кнопка мыши и функция очистить

#фунция для кнопки случайный, рамдомный цвет и выбор цвета для рисования
def RandomClick(event):
    global color
    color = '#%0x%0x%0x' % (randint(0,15), randint(0,15), randint(0,15))
    t = event.widget
    t['bg'] = color

#создание кнопки случайный
color_tmp = '#%0x%0x%0x' % (randint(0,15), randint(0,15), randint(0,15))
random_btn = Button(root, width = '9', bg = color_tmp, text = 'случайный')
random_btn.grid(row = 1, column = 5)
random_btn.bind('<Button-1>',RandomClick)#связать левая кнопка мыши и фукция случайный

# Создаем холст
picture = Canvas(root, width = 800, height = 800, bg = 'white')
picture.grid(column = 0, columnspan = 8, row = 2)

#функция для кнопки раскраска
def past (event):
    picture.delete('all')
    picture.create_image(10, 10, anchor=NW, image=image1)#открываем выбранную картинку в canavas
    
#создаём кнопку раскраска
pic = Button(width='9', bg='white', text='раскраска')
pic.grid(row=0, column=9, sticky='nw')
pic.bind('<Button-1>', past)

#рисование мышкой
#начальные координаты положения мыши
lastX, lastY = 0, 0
#начальный цвет
color = 'black'
#начальная толщина линии
t = 5
# Запоминаем координаты мыши в момент нажатия левой кнопки мыши
def onClick(event):
    global lastX, lastY 
    lastX = event.x #последняя кордината мыши x
    lastY = event.y #последняя кордината мыши y
#функция рисования линии
def onDrag(event):
    global lastX, lastY
    picture.create_line(lastX, lastY, event.x, event.y, fill = color, width = t)#рисование линии
    lastX = event.x #последняя кордината мыши x
    lastY = event.y #последняя кордината мыши y
# Связываем события нажатия левой кнопки мыши и последние кординаты
picture.bind('<Button-1>', onClick)
# Связываем события перемещения мыши с зажатой левой кнопкой и функцию рисования линии
picture.bind('<B1-Motion>', onDrag)

root.mainloop()

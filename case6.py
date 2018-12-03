"""Case-study #5 Тесселяция
Разработчики:
Shmatov D., Bayanova A.
"""

from turtle import *

#  get_num_hexagons - функция для ввода количества шестиугольников, предусматривающая проверку ввода данных.
#  Функция не имеет параметров и возвращает число от 4 до 20.
#  get_color_choice - функция для выбора цвета заливки шестиугольника. Функция не имеет параметров и возвращает строку - название цвета.
#  draw_hexagon - функция рисования шестиугольника. Функция ничего не возвращает и имеет следующие параметры:
#  x,y - координаты точки от которой рисуется фигура;
#  side_len - длина стороны;
#  color - цвет заливки фигуры.

def get_color_choice():
    colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    valid_input1 = False
    while not valid_input1:
            print("Меню доступных цветов: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый")
            color1 = input("Введите первый цвет: ")
            if color1 in colors:
                valid_input1 = True
            else:
                valid_input1 = False

    valid_input2 = False
    while not valid_input2:
            print("Меню доступных цветов: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый")
            color2 = input("Введите второй цвет: ")
            if color2 in colors:
               valid_input2 = True
            else:
               valid_input2 = False
    print("Выбранные цвета:", color1,",",color2,'.')

get_color_choice()

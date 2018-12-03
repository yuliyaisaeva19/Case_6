"""Case-study #5 Тесселяция
Разработчики:
Shmatov D., Bayanova A.
"""

from turtle import *

#  get_num_hexagons - функция для ввода количества шестиугольников, предусматривающая проверку ввода данных.
#  Функция не имеет параметров и возвращает число от 4 до 20.
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

def get_num_hexagons():
    ran = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    valid_input3 = False
    while not valid_input3:
        kol = input("Введите количество многоугольников (от 4 до 20): ")
        if kol in ran:
            valid_input3 = True
        else:
            valid_input3 = False
    print('Выбранное количество: ', kol)

get_color_choice()
get_num_hexagons()

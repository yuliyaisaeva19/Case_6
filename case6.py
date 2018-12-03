"""Case-study #5 Тесселяция
Разработчики:
Shmatov D., Bayanova A.
"""

from turtle import *

#  side_len - длина стороны;
#  color - цвет заливки фигуры.

def get_color_choice1():
    colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    valid_input1 = False
    while not valid_input1:
            print("Меню доступных цветов: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый")
            color1 = input("Введите первый цвет: ").lower()
            if color1 in colors:
                valid_input1 = True
            else:
                valid_input1 = False
    print("Выбранный первый цвет:", color1, '.')
    return turtle_colors(color1)

def get_color_choice2():
    colors = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    valid_input2 = False
    while not valid_input2:
            print("Меню доступных цветов: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый")
            color2 = input("Введите второй цвет: ").lower()
            if color2 in colors:
               valid_input2 = True
            else:
               valid_input2 = False
    print("Выбранный второй цвет:",color2,'.')
    return turtle_colors(color2)

def turtle_colors(x):
        if x == 'красный':
            x = 'red'
        elif x == 'синий':
            x = 'blue'
        elif x == 'зеленый':
            x = 'green'
        elif x == 'желтый':
            x = 'yellow'
        elif x == 'оранжевый':
            x = 'orange'
        elif x == 'пурпурный':
            x = 'purple'
        elif x == 'розовый':
            x == 'pink'


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

print(turtle_colors(get_color_choice1()))
print(turtle_colors(get_color_choice2()))
get_num_hexagons()


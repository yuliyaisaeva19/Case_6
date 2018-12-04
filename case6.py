"""Case-study #5 Тесселяция
Разработчики:
Shmatov D. 80%, Bayanova A. 70%
"""

from turtle import *

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
                print("Неверный ввод, попробуйте ещё раз.")
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
                print("Неверный ввод, попробуйте ещё раз.")
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
            x = 'pink'
        return x

def get_num_hexagons():
    ran = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    valid_input3 = False
    while not valid_input3:
        kol = input("Введите количество многоугольников (от 4 до 20): ")
        if kol in ran:
            valid_input3 = True
        else:
            valid_input3 = False
            print("Неверный ввод, попробуйте ещё раз.")
    print('Выбранное количество: ', kol)
    return kol



def size_hex(y):
    hex1 = 500/(2*y)
    side = hex1 * 2 / 3**0.5
    return side


def draw_hex(x):
    for i in range(0, 10):
        size = size_hex(x)
        forward(size)
        right(60)
    right(120)

def rows1(x,y):
        up()
        goto(-250, 250 - 500 / (2 * x) - (3 * y * size_hex(x)) - size_hex(x))
        down()

def rows2(x,y):
    up()
    goto(-250, 250 - 500 / (2 * x) - (3 * y * size_hex(x)) - size_hex(x))
    back(size_hex(x))
    right(60)
    back(size_hex(x))
    left(60)
    down()

def draw_picture(x, color1="yellow", color2="green"):
    col1 = color1
    col2 = color2
    if not x % 2:
        v = x
    if x % 2:
        v = x + 1
    for o in range(int(v)//2):
        rows1(x,o)
        for k in range(int(x)):
            if o % 2:
                color1, color2 = col2, col1
            if not o % 2:
                color1, color2 = col1, col2
            if not k % 2:
                fillcolor(color1)
            if k % 2:
                fillcolor(color2)
            begin_fill()
            draw_hex(x)
            end_fill()
    for t in range(int(x)//2):
        rows2(x,t)
        for k in range(int(x)):
            if t % 2:
                color1, color2 = col2, col1
            if not t % 2:
                color1, color2 = col1, col2
            if not k % 2:
                fillcolor(color1)
            if k % 2:
                fillcolor(color2)
            begin_fill()
            draw_hex(x)
            end_fill()

def first_pos(n):
    up()
    goto(-250, 250 - 500 / (2 * n))
    left(90)
    down()


def main():
    c1 = turtle_colors(get_color_choice1())
    c2 = turtle_colors(get_color_choice2())
    n = int(get_num_hexagons())
    Screen()
    screensize(500, 500)
    speed(0)
    first_pos(n)
    draw_picture(n, c1, c2)
    done()

if __name__ == '__main__':
    main()
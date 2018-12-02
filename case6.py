"""Case-study #5 Тесселяция
Разработчики:
Shmatov D., Bayanova A.
"""

from turtle import *

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

def rows(x):
    for i in range(int(x+1/2)):
        up()
        goto(-250, 250 - 500 / (2 * x) - (2 * i * size_hex(x)) - size_hex(x))
        down()

def draw(x, color1="yellow", color2="green"):
    for k in range(int(x)):
        if not k % 2:
            fillcolor(color1)
        if k % 2:
            fillcolor(color2)
        begin_fill()
        draw_hex(x)
        end_fill()
    up()
    goto(-250, 250 - 500 / (2 * x))
    right(60)
    back(size_hex(x))
    left(60)
    back(size_hex(x))
    down()
    for l in range(int(x)):
        if not l % 2:
            fillcolor(color1)
        if l % 2:
            fillcolor(color2)
        begin_fill()
        draw_hex(x)
        end_fill()
    rows(x)








def main():
    Screen()
    screensize(500, 500)
    speed(0)
    color = textinput("Color", "Write color of hexes").split()
    c1, c2 = map(str, color)
    n = numinput("Number of hexes", "Input number")
    up()
    goto(-250, 250 - 500 / (2 * n))
    left(90)
    down()
    for i in range(n)
    draw(n, c1, c2)
    done()

if __name__ == '__main__':
    main()
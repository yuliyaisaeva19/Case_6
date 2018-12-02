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

def draw(x, color1="yellow", color2="green"):
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
    draw(n, c1, c2)
    done()

if __name__ == '__main__':
    main()
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
    for i in range(0, 8):
        size = size_hex(x)
        right(60)
        forward(size)
    left(120)

def draw(x, color1="yellow", color2="green"):
    for k in range(int(x)):
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
    color = textinput("Color", "Write color of hexes").split()
    c1, c2 = map(str, color)
    n = numinput("Number of hexes", "Input number")
    up()
    goto(-250, 250 - 500 / (2 * n))
    left(90)
    down()
    size_hex(n)
    draw(n, c1, c2)
    done()

if __name__ == '__main__':
    main()
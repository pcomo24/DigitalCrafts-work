from turtle import *


def triangle(size, pen_color,fill_color):
    pencolor(pen_color)
    fillcolor(fill_color)
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size)


def square(size, obj_color):
    color(obj_color)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)


def pentagon(size, obj_color):
    color(obj_color)
    forward(size)
    left(90)
    forward(size)
    left(45)
    forward(size)
    left(90)
    forward(size)
    left(45)
    forward(size)
    left(90)
    forward(size)


def hexagon(size, obj_color):
    color(obj_color)
    for i in range(6):
        forward(size)
        left(60)


def octagon(size, obj_color):
    color(obj_color)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)


def star(size, obj_color):
    color(obj_color)
    for i in range(5):
        forward(size)
        right(144)

def mycircle(obj_color):
    color(obj_color)
    width(10)
    circle(180)

    mainloop()

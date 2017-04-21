from turtle import *
import random
bgcolor("black")
color("green")

def reset():
    up()
    home()

def draw(length):
    forward(length)
    up()

def resetpos(x,y):
    setpos(x,y)
    down()

def horiz():
    draw(10)
    resetpos(0,50)
    draw(10)
    resetpos(10,60)
    draw(10)

def angle():
    left(45)
    resetpos(10,0)
    draw(15)
    resetpos(10,20)
    draw(15)
    resetpos(20,30)
    draw(15)
    resetpos(20,40)
    draw(15)
    resetpos(10,50)
    draw(15)
    resetpos(0,50)
    draw(15)
    resetpos(10,30)
    draw(7.5)
    resetpos(5,30)
    draw(15)

def angle_op():
    left(-45)
    resetpos(10,50)
    draw(15)
    resetpos(20,60)
    draw(15)
    resetpos(10,45)
    draw(7.5)


def vert_s():
    left(90)
    resetpos(20,30)
    draw(10)
    resetpos(30,40)
    draw(10)

def vert_m():
    left(90)
    resetpos(10,0)
    draw(20)
    resetpos(20,10)
    draw(20)

def vert_l():
    left(90)
    down()
    draw(50)

def vert_il():
    left(-90)
    resetpos(5,45)
    draw(15)
    resetpos(15,40)
    draw(5)

def horiz_i():
    resetpos(5,30)
    draw(5)
    resetpos(5,45)
    draw(5)


horiz()
reset()
angle()
reset()
angle_op()
reset()
vert_s()
reset()
vert_m()
reset()
vert_l()
reset()
horiz_i()
reset()
vert_il()
reset()




mainloop()

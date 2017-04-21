from turtle import *
import random
bgcolor("black")
color("green")

def reset():
    up()
    home()
    down()

def draw(length):
    forward(length)
    up()
#cube
def horiz():
    forward(40)
    up()
    setpos(0,40)
    down()
    forward(40)
    up()
    setpos(20,60)
    down()
    forward(40)

def vert():
    left(90)
    forward(40)
    up()
    setpos(40,0)
    down()
    forward(40)
    up()
    setpos(60,20)
    down()
    forward(40)

def angl():
    left(45)
    up()
    setpos(0,40)
    down()
    forward(30)
    up()
    setpos(40,40)
    down()
    forward(30)
    up()
    setpos(40,0)
    down()
    forward(30)



horiz()
reset()
vert()
reset()
angl()


#setpos(random.randint(0,300),random.randint(0, 300))
#down()
mainloop()

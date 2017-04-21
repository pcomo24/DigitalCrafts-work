from turtle import *
import random
bgcolor("black")
color("yellow")
i = 0
while i < 20:
    for j in range(20):
        forward(12)
        up()
        backward(12)
        right(18)
        down()
    up()
    setpos(random.randint(0,300),random.randint(0, 300))
    down()
    i += 1

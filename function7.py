import matplotlib.pyplot as plot
from numpy import arange
import math
x = int(input("What is the temp in Celsius?"))
def f(x):
    return x * 1.8 + 32

def draw():
    xs = arange(-126, 136, 0.1)
    ys = []
    for x in xs:
        ys.append(f(x))
    plot.plot(xs, ys)
    plot.show()

if __name__ == "__main__":
    draw()

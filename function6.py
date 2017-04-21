import matplotlib.pyplot as plot
from numpy import arange
import math

def f(x):
    return math.sin(x)

def draw():
    xs = arange(-5, 5, 0.1)
    ys = []
    for x in xs:
        ys.append(f(x))
    plot.plot(xs, ys)
    plot.show()

if __name__ == "__main__":
    draw()

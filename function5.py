import matplotlib.pyplot as plot
import math
def f(x):
    return math.sin(x)

def draw():
    xs = list(range(-5, 5))
    ys = []
    for x in xs:
        ys.append(f(x))
    plot.plot(xs, ys)
    plot.show()

if __name__ == "__main__":
    draw()

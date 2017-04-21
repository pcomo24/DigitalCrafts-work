import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

def draw():
    xs = list(range(-5, 5))
    ys = []
    for x in xs:
        ys.append(f(x))
    plot.bar(xs, ys)
    plot.show()

if __name__ == "__main__":
    draw()

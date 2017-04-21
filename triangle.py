
xr = int(input("what is the triangle height?"))

for x in range(0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    print(' ' * spaces + '*' * stars)

width = int(input("width?"))
height = int(input("height?"))
print("*" * width)
for i in range(height - 2):
    print("*", end="")
    for j in range(width - 2):
        print(' ', end="")

    print("*")
print("*" * width)

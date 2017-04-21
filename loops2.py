start = int(input("what number to start with?"))
end = int(input("what number to end with?"))
number = 0
for number in range(start - 1, end):
    number += 1
    print(number)

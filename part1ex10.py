coins = 0
while True:
    print("You have {} coins.".format(coins))
    ans = input("do you want another? ")
    if ans == "no":
        break
    else:
        coins += 1

print("Bye")

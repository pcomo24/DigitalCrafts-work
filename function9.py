def replay():
    response = input("Do you want to play again(Y or N)? ")
    if response == "Y":
        return True
    elif response == "N":
        return False
    else:
        print("Invalid input")
        replay()

print(replay())

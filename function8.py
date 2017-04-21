def replay():
    response = input("Do you want to play again(Y or N)?")
    if response.upper() == "Y":
        return True
    else:
        return False

replay()
if True:
    print("ok, let's play again")
if False:
    print("ok, see ya later")

print("I am thinking of a number between 1 and 10.")
secret_number = 5
while True:
    guess = int(input("What's the number? "))
    if guess == 5:
      print("Yes! You win!")
      break
    else:
      print("Nope, try again")

import random
my_random_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
print("You have 5 guesses left.")
guess_count = 0
while guess_count < 5:
    guess = int(input("What's the number? "))
    if guess == my_random_number:
      print("Yes! You win!")
      break
    elif guess > my_random_number:
      guess_count += 1
      print("{} is too high.".format(guess))
      print("you have {} guesses left".format(guess_count))
    else:
      guess_count += 1
      print("{} is too low.".format(guess))
      print("you have {} guesses left".format(guess_count))

print("You ran out of guesses!")

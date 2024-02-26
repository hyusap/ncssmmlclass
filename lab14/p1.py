import random


# guessing game
def guessing_game():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    guess = int(input("Your guess: "))
    while guess != number:
        if guess < number:
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")
        guess = int(input("Your guess: "))
    print("You guessed it! The number was", number)


guessing_game()

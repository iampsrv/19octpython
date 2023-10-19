import random
print("Guess the number")

def play_game():
    number = random.randint(1, 10)
    max_number_of_guesses = 10
    guess = int(input("Guess the number between 1 and 10: "))
    # while guess != number:
    for i in range(max_number_of_guesses):
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("You guessed it correctly")
            break
        guess = int(input("Guess the number between 1 and 10: "))
    else:
        print("You failed to guess the number correctly")
play_game()
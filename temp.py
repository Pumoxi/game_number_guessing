import random
from art import logo

# Define Global Variable

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def generate_random_number():

    '''Generate random number between 1 and 100, and return the number as integer.'''

    # generate random number between 1 and 100
    return random.randint(1, 100)

def set_difficulty():

    '''Set the difficulty of the game, and return the number of attempts.'''

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_ATTEMPTS
    elif difficulty == "hard":
        return HARD_ATTEMPTS

def guess_number(random_number, guess):
    
    '''Compare the guess with the random number, and return True if the guess is correct, otherwise return False.'''

    if guess > random_number:
        print("Too high.")
        print("Guess again.")
        return False
    elif guess < random_number:
        print("Too low.")
        print("Guess again.")
        return False
    else:
        print(f"You got it! The answer was {random_number}.")
        return True

def play_game():

    print(logo)

    '''Play the game.'''

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Gent the attempts count
    attempts = set_difficulty()

    correct_guess = False
    random_number = generate_random_number()

    while not correct_guess:

        print(f"You have {attempts} attempts remaining to guess the number.")

        if attempts > 0:
            guess = int(input("Make a guess: "))
            correct_guess = guess_number(random_number, guess)
            attempts -= 1
        else:
            print("You've run out of guesses, you lose.")
            break

if __name__ == "__main__":
    play_game()
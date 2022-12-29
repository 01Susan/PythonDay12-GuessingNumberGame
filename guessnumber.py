from random import randint
from art import logo

easy_level_turns = 10
hard_level_turns = 5


def check_answer(guess, answer, turns):
    """Checking the guessed number with our answer"""
    if guess > answer:
        print("Too high")
        turns -= 1
    elif guess < answer:
        print("Too low")
        turns -= 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    """Can choose the diffculty level 'Easy' or 'Hard'.easy = 10 atempts and hard = 5 attempt)"""
    level = input("Chosse a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is 45 ")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess=guess, answer=answer, turns=turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

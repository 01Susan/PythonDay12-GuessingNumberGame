from random import randint
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Pssst, the correct answer is 2")


def gameplay():
    easy_level = 10
    hard_level = 5
    is_game_over = False
    random_int = randint(0, 100)

    def compare():
        if number_guess == random_int:
            global is_game_over
            is_game_over = True
        elif number_guess < random_int:
            print("Too Low")
        elif number_guess > random_int:
            print("Too High")

    def winner():
        if is_game_over == True:
            print(f"You guess the word")
        else:
            print(f"The word was {random_int}.You are not able to guess the word.")

    level_option = input("Choose a difficulty.Type 'easy' or 'Hard': ").lower()
    if level_option == "easy":

        while easy_level > 0 or is_game_over == True:
            print(f"You have {easy_level} attempts remaining to guess the number.")
            number_guess = int(input("Make a guess: "))
            easy_level -= 1
            compare()

    else:
        while hard_level > 0 or is_game_over == True:
            print(f"You have {hard_level} attempts remaining to guess the number.")
            number_guess = int(input("Make a guess: "))
            hard_level -= 1
            compare()


gameplay()

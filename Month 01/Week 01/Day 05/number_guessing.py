import random
from art import logo

EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print('Your guess is too high')
        return turns - 1
    elif guess < answer:
        print('Your answer is too low')
        return turns - 1
    else:
        print(f'You go it! The answer was {answer}')

def set_difficulty():
    '''chooses a difficulty level'''
    level = input("Would you like to play on 'easy' or 'hard'?  ")
    if level == 'easy':
        return EASY
    elif level == 'hard':
        return HARD
    else:
        print("Please choose either 'easy' or 'hard' only.")

def play_game():
    print(logo)
    print('Welcome to Guess The Number')
    print('I am thinking of a number between 1 and 100, can you guess it?')
    answer = random.randint(1,101)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f'You have {turns} left to answer.')
        guess = int(input("Make a guess:  "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You are out of guesses, you lose!')
            return
        elif guess != answer:
            print('Guess again.')

play_game()

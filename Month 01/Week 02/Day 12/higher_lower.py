import random
from art import logo, vs
from game_data import data
from os import system, name
from time import sleep

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_descr}, from {account_country}'

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check_answer(guess, a_followers, b_followers):
    """Take users guess and followers counts and return it the got it right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)},')
    print(vs)
    print(f'Against B: {format_data(account_b)},')

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'a' or 'b':  ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Feedback.
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry thats wrong. Final Score: {score}")
# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
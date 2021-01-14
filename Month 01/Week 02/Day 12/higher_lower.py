import random
from art import logo, vs
from game_data import data


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_descr}, from {account_country}'

def check_answer(guess, a_followers, b_followers):
    """Take users guess and followers counts and return it the got it right"""

print(logo)
# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
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

## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
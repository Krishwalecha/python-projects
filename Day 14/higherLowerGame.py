from game_data import data
import art
import random
import os

def format_name(details):
    """Takes a person's details (dictionary) and returns formatted info."""
    username = details["name"]
    followers = details["follower_count"]
    desc = details["description"]
    country = details["country"]
    return username, followers, desc, country

def clear_screen():
    # Clears user terminal
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\033c", end="")

score = 0
print(art.logo)

a_details = random.choice(data)

while True:
    # Make sure B is different from A
    while True:
        b_details = random.choice(data)
        if b_details != a_details:
            break

    # Formatted values
    a_name, a_followers, a_description, a_country = format_name(a_details)
    b_name, b_followers, b_description, b_country = format_name(b_details)

    # Display comparison
    article = 'an' if a_description[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    print(f"\nCompare A: {a_name}, {article} {a_description}, from {a_country}")
    print(art.vs)
    article = 'an' if b_description[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    print(f"Compare B: {b_name}, {article} {b_description}, from {b_country}\n")

    # Get user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    while guess not in ['A', 'B']:
        guess = input("Invalid input. Please type 'A' or 'B': ").upper()

    # Check guess
    correct = 'A' if a_followers > b_followers else 'B'
    if guess == correct:
        score += 1
        clear_screen()
        print(art.logo)
        print(f"You're right! {guess} has more followers than {'B' if guess == 'A' else 'A'}. Current score: {score}")
        a_details = b_details  # Move B to A for next round
    else:
        clear_screen()
        print(art.logo)
        print(f"You lost. {correct} has more followers than {guess}. Final score: {score}\n")
        new_game = input("Do you want to play again? (Yes/No): ").capitalize()

        if new_game == 'Yes':
            clear_screen()
            print(art.logo)
            score = 0
            a_details = random.choice(data)
        else:
            print("Goodbye! 👋")
            break

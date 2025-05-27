import random
import art
import os

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5
CLOSE_MARGIN = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_number(difficulty_level):
    while True:
        number = random.randint(10, 999)
        if (difficulty_level == 'easy' and number < 100) or (difficulty_level == 'hard' and number >= 100):
            return number

def assign_lives(difficulty_level):
    return EASY_LEVEL_LIVES if difficulty_level == 'easy' else HARD_LEVEL_LIVES

def play_game(score):
    # Input difficulty with validation
    while True:
        difficulty = input('Choose your difficulty (easy/hard): ').strip().lower()
        if difficulty in ('easy', 'hard'):
            break
        print("Invalid input. Please type 'easy' or 'hard'.")

    chosen_number = pick_number(difficulty)
    print(f"\nThe chosen number has {len(str(chosen_number))} digits.")

    lives = assign_lives(difficulty)
    guessed_numbers = []

    print(f"You have {lives} lives to guess the number.")
    
    while True:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess in guessed_numbers:
            print(f"You have already guessed {guess}. Try again.")
            continue

        guessed_numbers.append(guess)

        if guess == chosen_number:
            print(f"You won! The number was indeed {chosen_number}.")
            score += 1
            break
        else:
            if abs(guess - chosen_number) <= CLOSE_MARGIN:
                print("You are very close!")
            elif guess > chosen_number:
                print("Too high!")
            else:
                print("Too low!")

        lives -= 1
        print(f"Lives remaining: {lives}\n")

        if lives == 0:
            print(f"You ran out of lives. You lose. The number was {chosen_number}.")
            break

    return score

# Game loop with score tracking
score = 0

while True:
    print(art.numberGuessingGameArt)
    print(f"\nCurrent Score: {score}")
    score = play_game(score)

    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay not in ('yes', 'y'):
        print(f"Thanks for playing! Your final score: {score}")
        break
    clear_screen()

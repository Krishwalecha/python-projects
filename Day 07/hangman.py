import random
from words import words_list
from hangmanArt import HANGMANPICS

def hangman():
    print("Welcome to the Hangman Challenge!")

    # Ask player to select difficulty and validate input
    difficulty = input("Select difficulty level (Easy/Hard): ").capitalize()
    while difficulty not in ['Easy', 'Hard']:
        difficulty = input("Invalid input. Please enter 'Easy' or 'Hard': ").capitalize()

    # Choose a word matching difficulty
    while True:
        chosen_word = random.choice(words_list)
        if (difficulty == 'Easy' and len(chosen_word) <= 6) or (difficulty == 'Hard' and len(chosen_word) > 6):
            break

    # Prepare the word display with underscores
    word_display = ["_"] * len(chosen_word)
    print(f"\nThe secret word contains {len(chosen_word)} letters.")
    print(" ".join(word_display))

    # Ask if player wants to guess the whole word at once
    choice = input("Would you like to guess the entire word at once? (Yes/No): ").capitalize()
    while choice not in ['Yes', 'No']:
        choice = input("Invalid input. Please enter 'Yes' or 'No': ").capitalize()

    if choice == "No":
        lives = 6
        guessed_letters = []
        print(f"\nYou have {lives} chances. Let's begin!")
    else:
        print("\nYou have one chance to guess the entire word correctly.")

    # Main game loop
    while True:
        if choice == "Yes":
            guess = input("Enter your guess for the whole word: ")
            if guess == chosen_word:
                print(f"Congratulations! You correctly guessed the word: {chosen_word}")
            else:
                print(f"Incorrect! The correct word was: {chosen_word}")
            break

        else:
            guess = input("Guess a letter: ").lower()

            # Validate that input is a single alphabetic character
            while len(guess) != 1 or not guess.isalpha():
                guess = input("Invalid input. Please guess a single letter (a-z): ").lower()

            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try a different letter.")
            else:
                guessed_letters.append(guess)

                if guess in chosen_word:
                    # Reveal guessed letters
                    for index, letter in enumerate(chosen_word):
                        if letter == guess:
                            word_display[index] = guess
                    print(f"✅ Nice! The letter '{guess}' is in the word.")
                else:
                    lives -= 1
                    print(f"❌ Oops! The letter '{guess}' isn't in the word. You lost a life.")

            # Show current status
            print(f"\nLives remaining: {lives}")
            print(HANGMANPICS[6 - lives])
            print("Current progress: " + " ".join(word_display))
            print(f"Guessed letters so far: {', '.join(guessed_letters)}\n")

            # Check end conditions
            if lives == 0:
                print(f"Game Over! The correct word was: {chosen_word}")
                break
            elif "_" not in word_display:
                print(f"Excellent! You've uncovered the word: {chosen_word}")
                break

# Loop to allow replay
while True:
    hangman()
    replay = input("Would you like to play another round? (Yes/No): ").capitalize()
    while replay not in ['Yes', 'No']:
        replay = input("Invalid input. Please type 'Yes' or 'No': ").capitalize()
    if replay == "No":
        print("Thanks for playing Hangman! See you next time.")
        break

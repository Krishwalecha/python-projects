import random
import art
import os

# List of card values (Ace=11, face cards=10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(number):
    return random.choices(cards, k=number)

def convert_ace(hand):
    # Corrected: convert all Aces if total > 21
    while 11 in hand and sum(hand) > 21:
        index = hand.index(11)
        hand[index] = 1
    return hand

def decide_winner(user_hand, computer_hand):
    user_score = sum(user_hand)
    comp_score = sum(computer_hand)

    print()

    if user_score == 21 and len(user_hand) == 2:
        print("Blackjack! You win!")
    elif comp_score == 21 and len(computer_hand) == 2:
        print("Computer got Blackjack! You lose!")
    elif user_score > 21 and comp_score > 21:
        print("Both busted! You lose!")
    elif user_score > 21:
        print("You busted. You lose!")
    elif comp_score > 21:
        print("Computer busted. You win!")
    elif user_score == comp_score:
        print("It's a draw.")
    elif user_score > comp_score:
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_cards = draw_cards(2)
    computer_cards = draw_cards(2)

    user_cards = convert_ace(user_cards)
    computer_cards = convert_ace(computer_cards)

    print(f"\nYour Cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}\n")

    while sum(user_cards) < 21:
        draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if draw == 'n':
            break
        elif draw == 'y':
            user_cards += draw_cards(1)
            user_cards = convert_ace(user_cards)
            print(f"\nYour current hand: {user_cards}")
        else:
            print("\nInvalid input. Please type 'y' or 'n'.\n")

    print(f"Your final hand: {user_cards} (Total: {sum(user_cards)})\n")

    while sum(computer_cards) < 17:
        computer_cards += draw_cards(1)

    computer_cards = convert_ace(computer_cards)
    print(f"Computer's final hand: {computer_cards} (Total: {sum(computer_cards)})")

    decide_winner(user_cards, computer_cards)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print(art.blackjack)
        play_game()
        again = input("Play again? Type 'y' for yes, 'n' for no: ").lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye.\n")
            break
        else:
            clear_screen()

if __name__ == "__main__":
    main()

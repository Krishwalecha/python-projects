import random
from art import caesarCipher  # ASCII art for title or logo (optional)

# Base alphabet: all lowercase and uppercase letters (total 52 characters)
base_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def select_alphabet():
    """
    Ask user whether to use a shuffled or unshuffled alphabet.
    Returns:
        alphabets (list): the chosen alphabet list
        alpha_type (str): 'shuffled' or 'unshuffled'
    """
    use_shuffle = input("Use shuffled alphabet? (yes/no): ").strip().lower()
    if use_shuffle == 'yes':
        # Create a copy of base alphabet and shuffle it randomly
        shuffled = base_alphabet[:]
        random.shuffle(shuffled)
        return shuffled, 'shuffled'
    else:
        # Use the original ordered alphabet
        return base_alphabet, 'unshuffled'

def get_shift_number(prompt):
    """
    Prompt user for a valid shift number between 1 and 51.
    Keeps asking until a valid integer in range is provided.
    """
    while True:
        try:
            shift = int(input(prompt))
            if 1 <= shift <= 51:
                return shift
            else:
                print("Shift must be between 1 and 51.")
        except ValueError:
            print("Please enter a valid integer.")

def caesar_cipher(message, shift_count, direction, alphabets):
    """
    Encrypt or decrypt a message using the Caesar cipher method
    with a custom alphabet.
    
    Args:
        message (str): the text to encode/decode
        shift_count (int): number of positions to shift
        direction (str): 'encode' or 'decode'
        alphabets (list): alphabet list used for substitution
    """
    processed_message = ""
    for char in message:
        if char not in alphabets:
            # Non-alphabet characters remain unchanged
            processed_message += char
        else:
            idx = alphabets.index(char)
            if direction == 'encode':
                shifted_idx = (idx + shift_count) % 52
            else:  # decode
                shifted_idx = (idx - shift_count) % 52
            processed_message += alphabets[shifted_idx]

    print(f"\nYour {direction}d message is: {processed_message}\n")

def main():
    # Print ASCII art title/logo
    print(caesarCipher)

    while True:
        # Ask user whether to encode or decode
        action = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
        if action not in ['encode', 'decode']:
            print("Invalid choice. Please try again.")
            continue

        if action == 'encode':
            # Select alphabet type (shuffled or unshuffled)
            alphabets, alpha_type = select_alphabet()

            message = input(f"Enter your message to {action}: ")

            # Ask if user wants a random shift number or manual input
            shift_choice = input("Do you want a random shift number? (yes/no): ").lower()
            if shift_choice == 'yes':
                shift = random.randint(3, 50)  # Random shift between 3 and 50
            else:
                shift = get_shift_number("Enter a shift number (1-51): ")

            # Perform encoding
            caesar_cipher(message, shift, action, alphabets)

            # Show info needed for decoding later
            print("Save this info for decoding:")
            print(f"Alphabet type: {alpha_type}")
            if alpha_type == 'shuffled':
                print(f"Alphabet list: {''.join(alphabets)}")
            print(f"Shift number: {shift}\n")

        else:  # decode
            # Ask if alphabet was shuffled during encoding
            was_shuffled = input("Was the alphabet list shuffled during encoding? (yes/no): ").strip().lower()
            if was_shuffled == 'yes':
                # User must enter the shuffled alphabet list used in encoding
                alphabets_input = input("Enter the shuffled alphabet used during encoding (52 characters): ")
                # Validate length and characters
                if len(alphabets_input) != 52 or set(alphabets_input) != set(base_alphabet):
                    print("Invalid shuffled alphabet entered. Exiting decoding.")
                    continue
                alphabets = list(alphabets_input)
            else:
                alphabets = base_alphabet

            message = input(f"Enter your message to {action}: ")
            shift = get_shift_number("Enter the shift number used for encoding: ")

            # Perform decoding
            caesar_cipher(message, shift, action, alphabets)

        # Ask if user wants to run again or exit
        again = input("Type 'yes' to go again or 'no' to exit: ").lower()
        print()
        if again == 'no':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

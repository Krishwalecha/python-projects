import pandas

data = pandas.read_csv(r'Day 26\nato_phonetic_alphabet.csv')
nato_dict = {row.letter : row.code for (index, row) in data.iterrows()}

while True:
    user_input = input("Enter a word: ").upper().replace(" ", "")
    try:
        nato_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Invalid input: Please enter only alphabetic characters (A-Z). Try again.")
    else:
        break

print(nato_list)
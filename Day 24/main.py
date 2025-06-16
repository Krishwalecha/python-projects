invited_names = []

with open(r"Day 24\Input\Names\invited_names.txt") as names_file:
    raw_names = names_file.readlines()

for raw_name in raw_names:
    invited_names.append(raw_name.strip())

with open(r"Day 24\Input\Letters\starting_letter.txt") as letter_file:
    letter_template = letter_file.read()

for invited_name in invited_names:
    personalized_letter = letter_template.replace("[name]", invited_name)

    with open(fr"Day 24\Output\ReadyToSend\{invited_name}.txt", mode="w") as output_file:
        output_file.write(personalized_letter)
    
    print(f"{invited_name}.txt created successfully!")

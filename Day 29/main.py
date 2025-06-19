from tkinter import *
from tkinter import messagebox
import random
import os
import json

# Constants
FONT = ("Arial", 12)
ALPHABETS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
SYMBOLS = list('~`!@#$%^&*()_-+|:;<>')
NUMBERS = list('1234567890')
PASSWORD_FILE = os.path.join('Day 29', 'passwords.json')

# --------------------- Password Generator --------------------- #
def generate_password():
    password_list = (
        random.choices(ALPHABETS, k=random.randint(4, 8)) +
        random.choices(SYMBOLS, k=random.randint(2, 6)) +
        random.choices(NUMBERS, k=random.randint(2, 6))
    )
    random.shuffle(password_list)
    password = "".join(password_list)
    password_output.delete(0, END)
    password_output.insert(0, password)

    # Copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    clipboard.config(text="Password copied to clipboard")

# --------------------- Save Password --------------------- #
def save_to_manager():
    website_input_raw = website_input.get().strip()
    website_key = website_input_raw.title()  # Capitalize for JSON key
    username = username_input.get().strip()
    generated_password = password_output.get().strip()

    new_data = {
        website_key: {
            "Username": username,
            "Password": generated_password
        }
    }

    if not website_input_raw or not username or not generated_password:
        messagebox.showwarning(title="Missing Information", message="All fields must be filled out.")
        return

    is_ok = messagebox.askokcancel(
        title="Confirm Save",
        message=f"Do you want to save this entry?\n\nWebsite: {website_key}\nUsername: {username}\nPassword: {generated_password}"
    )

    if is_ok:
        try:
            with open(PASSWORD_FILE, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open(PASSWORD_FILE, 'w') as file:
            json.dump(data, file, indent=4)

        website_input.delete(0, END)
        password_output.delete(0, END)

# --------------------- Search Function --------------------- #
def search():
    website_key = website_input.get().strip().title()  # Capitalize input to match key format

    try:
        with open(PASSWORD_FILE, 'r') as file:
            data = json.load(file)
            entry = data[website_key]
    except FileNotFoundError:
        messagebox.showinfo(title="Search Result", message="Password file not found.")
    except KeyError:
        messagebox.showinfo(title="Search Result", message="No entry found for the given website.")
    else:
        messagebox.showinfo(
            title="Credentials Found",
            message=f"Website: {website_key}\nUsername: {entry['Username']}\nPassword: {entry['Password']}"
        )
        window.clipboard_clear()
        window.clipboard_append(entry['Password'])

# --------------------- UI Setup --------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file=os.path.join('Day 29', 'password_system.png'))
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, pady=(0, 20))

# Feedback label
clipboard = Label(text="", fg='green', font=FONT)
clipboard.grid(column=1, row=5, columnspan=2, pady=(10, 0))

# Website
Label(text="Website:", font=FONT).grid(column=0, row=1, sticky="e", padx=5, pady=5)
website_input = Entry(width=21, font=FONT)
website_input.grid(column=1, row=1, sticky="w", pady=5)

search_button = Button(text="Search", width=12, font=FONT, command=search)
search_button.grid(column=2, row=1, padx=5)

# Email/Username
Label(text="Email or Username:", font=FONT).grid(column=0, row=2, sticky="e", padx=5, pady=5)
username_input = Entry(width=35, font=FONT)
username_input.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)
username_input.insert(0, "example@email.com")

# Password
Label(text="Password:", font=FONT).grid(column=0, row=3, sticky="e", padx=5, pady=5)
password_output = Entry(width=21, font=FONT)
password_output.grid(column=1, row=3, sticky="w", pady=5)

generate_password_button = Button(text="Generate", font=FONT, width=12, command=generate_password)
generate_password_button.grid(column=2, row=3, padx=5)

# Add Button
add_button = Button(text="Save Password", width=35, font=FONT, command=save_to_manager)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=(10, 0))

window.mainloop()

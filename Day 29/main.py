from tkinter import *
from tkinter import messagebox
import random
import os

FONT = ("Arial", 12)
ALPHABETS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
SYMBOLS = list('~`!@#$%^&*()_-+|:;<>')
NUMBERS = list('1234567890')

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

# --------------------- Manager Setup --------------------- #
def save_to_manager():
    website = website_input.get().strip()
    username = username_input.get().strip()
    generated_password = password_output.get().strip()

    if not website or not username or not generated_password:
        messagebox.showwarning(title="Missing Info", message="Please fill in all fields.")
        return

    is_ok = messagebox.askokcancel(
        title="Save Password?",
        message=f"Save the following entry?\n\nWebsite: {website}\nUsername: {username}\nPassword: {generated_password}"
    )

    if is_ok:
        try:
            with open(r'Day 29\passwords.txt', mode='a') as data:
                data.write(f"{website} | {username} | {generated_password}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the password: {e}")
        else:
            website_input.delete(0, END)
            password_output.delete(0, END)

# --------------------- UI Setup --------------------- #
window = Tk()
window.title("Password Generator and Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file=os.path.join('Day 29', 'password_system.png'))
canvas.create_image(100, 100, image=img)
clipboard = Label(fg='green', font=(FONT, 12))
canvas.grid(column=1, row=0, pady=(0, 20))
clipboard.grid(column=1, row=5, columnspan=2, pady=(10, 0))

# Website
website_name_label = Label(text="Website:", font=FONT)
website_name_label.grid(column=0, row=1, sticky="e", padx=5, pady=5)
website_input = Entry(width=35, font=FONT)
website_input.grid(column=1, row=1, columnspan=2, sticky="w", pady=5)

# Email/Username
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(column=0, row=2, sticky="e", padx=5, pady=5)
username_input = Entry(width=35, font=FONT)
username_input.grid(column=1, row=2, columnspan=2, sticky="w", pady=5)
username_input.insert(0, "example@email.com")  # Default email

# Password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)
password_output = Entry(width=21, font=FONT)
password_output.grid(column=1, row=3, sticky="w", pady=5)

# Generate Password Button
generate_password_button = Button(text="Generate", font=FONT, width=11, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w", pady=5)

# Add Button
add_button = Button(text="Add to Password Manager", width=34, font=FONT, command=save_to_manager)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=(10, 0))

window.mainloop()

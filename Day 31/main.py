import tkinter
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- LOAD DATA ------------------------------- #
# Try to load the list of words to learn; if not found, load full list
try:
    data = pandas.read_csv(r'Day 31\data\words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv(r'Day 31\data\french_words.csv')

words_list = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    words_list.remove(current_card)
    new_data = pandas.DataFrame(words_list)
    new_data.to_csv(r'Day 31\data\words_to_learn.csv', index=False)
    new_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = tkinter.PhotoImage(file=r'Day 31\images\card_front.png')
card_back_img = tkinter.PhotoImage(file=r'Day 31\images\card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = tkinter.PhotoImage(file=r'Day 31\images\wrong.png')
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_img = tkinter.PhotoImage(file=r'Day 31\images\right.png')
right_button = tkinter.Button(image=right_img, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

new_card()

window.mainloop()

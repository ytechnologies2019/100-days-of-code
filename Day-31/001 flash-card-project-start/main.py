import random
import tkinter as tk
from tkinter import PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Load data
try:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    to_learn = [{"French": "Erreur", "English": "Error"}]  # Fallback data

current_card = {}


# Function to show the next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Reset timer when switching cards
    current_card = random.choice(to_learn)

    # Show French side
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # Flip after 3 seconds
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# Create window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer for auto-flip
flip_timer = window.after(3000, flip_card)

# Create Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')

card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = tk.Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

# Show the first card
next_card()

# Run the application
window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import tkinter
from tkinter import Canvas, PhotoImage, image_names, Button, Label, Entry, Radiobutton
import random
import pandas as pd
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')

window.config(padx=50 , pady=50)

canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 ,image=logo_img)
canvas.grid(row=0 , column=1)

##Labels
website_label  = Label(text='Website')
website_label.grid(row=1 , column=0)
email_label    = Label(text='Email/Username')
email_label.grid(row=2 , column=0)
password_label = Label(text='password')
password_label.grid(row=3 , column=0)

##Entry
website_entry  = Entry(width=35)
website_entry.grid(row=1 , column=1 , columnspan=2)
website_entry.insert(0 , '')

email_entry    = Entry(width=35)
email_entry.grid(row=2 , column=1 , columnspan=2)
email_entry.insert(0 , '')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=2)

##Generate Password
def password_generate():
    password_length = random.randint(8,16)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_entry.insert(0, password)

##Generate Password Buttons
generate_password_button = Button(text="Generate Password" , command = password_generate)
generate_password_button.grid(row=3 , column=2 , columnspan=2)

def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create a dictionary with the data
    data = {
        'Website': [website],
        'Email': [email],
        'Password': [password]
    }
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Append data to the CSV file without headers
    df.to_csv('password.csv', mode='a', index=False , header=False)

    # Clear the entry fields after saving
    website_entry.delete(0, tkinter.END)
    email_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
##Add Button
add_button               = Button(text="Add" , width=36, command=save_info )
add_button.grid(row=4 , column=1 , columnspan=2)

window.mainloop()
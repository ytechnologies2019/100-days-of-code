import tkinter
import turtle as t
from tkinter import Button, Entry
from turtle import Screen

windows = tkinter.Tk()

windows.title("Welcome to Tkinter")
windows.minsize(width=500, height=300)
windows.config(padx=100 , pady=300)

# Label
my_label = tkinter.Label(text="I am Label", font=("Arial" , 30, "bold"))
my_label = tkinter.Label()
# my_label.pack(expand='True')
# my_label.place(x=100 , y=200)
##Grid

my_label.grid(column=0 , row=0)

my_label.config(text="New Text") ## Replace to old label

##Button
# my_button = tkinter.Button(text='Click me')
# my_button.pack()
def click():
   new_text = input.get()
   my_label.config(text=new_text)


button = Button(text="Click Me" , command=click)
# button.pack()
button.grid(column=4 , row=4)

##New_Button
new_button = Button(text="New_Button" , command=click)
button.grid(column=4,row=0)

tim = t.Turtle()
tim.write("Some Texts", align="center", font=("Arial", 50, "bold"))
screen = Screen()


# Start the Tkinter event loop
#Entry Class
input = Entry()
# input.pack()
print(input.get())
input.grid(column=2 , row=2)
new_button.grid()
windows.mainloop()
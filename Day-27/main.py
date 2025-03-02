import tkinter as tk

## Screen Setup
screen = tk.Tk()
screen.title("Welcome to Calculator")
screen.geometry('500x500')

## Text Boxes
kilo_text_box = tk.Text(width=6, height=2, font=('Arial', 20))
kilo_text_box.pack()
kilo_label = tk.Label(text="Kilometer", font="Arial")
kilo_label.pack()



# Font Setup
label = tk.Label(text="Mile to Kilometer Calculator", font=('Arial', 35), pady=30)
label.pack()

mile_label = None
mile_result_label = None

def button_click():
    global mile_label, mile_result_label

    # Clear previous result labels if they exist
    if mile_label:
        mile_label.destroy()
    if mile_result_label:
        mile_result_label.destroy()

    kilo_value = (kilo_text_box.get("1.0", tk.END).strip())
    if kilo_value:
        # Mile Label (instead of Text Box)
        mile_label = tk.Label(text="The result will display at below 👇👇", font="Arial", pady=10)
        mile_label.pack()
        mile_result_label = tk.Label(text="", font="Arial", width=10, height=2)
        mile_result_label.pack()
        kilo_value = float(kilo_value)
        convert_to_mile = kilo_value * 0.62137119
        mile_result_label.config(text=f"{convert_to_mile:.2f} Miles")  # Update the label with the result


button = tk.Button(text="Convert", font=('Arial', 20), command=button_click)
button.pack()

tk.mainloop()

from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons

def button_clicked():
    print("I got clicked")
    new_label = input.get()
    my_label.config(text=new_label)


button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="Button 2", command=button_clicked)
button.grid(column=1, row=1)
button2.grid(column=3, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=2)


# Grid


window.mainloop()
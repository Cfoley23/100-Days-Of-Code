from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    output.config(text=f"{km}")

window = Tk()
window.minsize(width=400, height=200)
window.title("Mile(s) to Kilometer(s) Converter")
window.config(padx=100, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Mile(s)", font=("Arial"))
miles_label.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial"))
equal_to.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial"))
km_label.grid(column=2, row=1)

output = Label(text="0", font=("Arial"))
output.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)




window.mainloop()
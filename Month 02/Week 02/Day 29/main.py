from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)
email_username_label = Label(text="E-mail/Username:", font=("Arial", 12))
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 12))
password_label.grid(column=0, row=3)
add_button = Button(width=10, text="ADD", font=("Arial", 12))
add_button.grid(column=1, row=4, columnspan=3)
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry = Entry(width=36)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", font=("Arial"))
password_button.grid(column=2, row=3)


window.mainloop()

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website}  ][  {email}  ][  {password}")
        website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)
email_username_label = Label(text="E-mail/Username:", font=("Arial", 12))
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 12))
password_label.grid(column=0, row=3)
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=36)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "youraddress@email.com")
password_entry = Entry(width=36)
password_entry.grid(column=1, row=3, columnspan=2)
password_button = Button(width=24, text="Generate Password", font=("Arial"))
password_button.grid(column=1, row=4)
add_button = Button(width=24, text="ADD", font=("Arial", 12))
add_button.grid(column=1, row=5)

window.mainloop()

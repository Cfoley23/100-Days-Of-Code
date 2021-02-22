from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Don't leave any fields blank.")
    else:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
            # updating old data with new data
            data.update(new_data)

        with open("data.json", "r") as data_file:
            # saving the updated data
            json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

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
password_button = Button(width=24, text="Generate Password", font="Arial", command=generate_password)
password_button.grid(column=1, row=4)
add_button = Button(width=24, text="ADD", font=("Arial", 12), command=save)
add_button.grid(column=1, row=5)

window.mainloop()

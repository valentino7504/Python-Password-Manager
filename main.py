from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()


# ----------------------------- PASSWORD RETRIEVAL --------------------------------#
def search():
    website = website_entry.get().title()
    try:
        with open("modules/data.json", mode="r") as data:
            details = json.load(data)
    except (FileNotFoundError, KeyError):
        messagebox.showerror(title="Error", message="No Data File")
    else:
        if website in details:
            username = details[website]["username"]
            password = details[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Username: {username} \nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    password = password_generator.generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get().strip().title()
    username = email_entry.get().strip()
    password = password_entry.get().strip()
    if len(website_name.strip()) == 0 or len(username.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showerror(title="Error", message="Blank field(s) detected")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered:\n\nEmail/Username: {username}\n"
                                               f"Password: {password}\n\n"
                                               f"Is it okay to save?")
        if is_ok:
            new_data = {website_name: {
                "username": username,
                "password": password
            }
            }
            try:
                with open("modules/data.json", mode="r") as data:
                    details = json.load(data)
            except FileNotFoundError:
                with open("modules/data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("modules/data.json", mode="w") as data:
                    details.update(new_data)
                    json.dump(details, data, indent=4)
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, "my_email@gmail.com")
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=20, width=1000)

canvas = Canvas()
canvas.config(height=200, width=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1, columnspan=2, sticky="W")

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=23)
website_entry.grid(row=1, column=1, pady=20)
website_entry.focus()
website_button = Button(text="Search", width=14, command=search)
website_button.grid(row=1, columnspan=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2, pady=20)
email_entry.insert(0, "edwinmbonyjr@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, columnspan=1, pady=20)
password_button = Button(text="Generate Password", width=14, command=generate)
password_button.grid(row=3, columnspan=1, column=2)

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=20)

window.mainloop()

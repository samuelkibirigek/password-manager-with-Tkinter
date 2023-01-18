from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    number_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, f"{password}")

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get()
    username = username_input.get()
    new_password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(new_password) == 0:
        messagebox.showwarning(title=website, message="Kindly fill in all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Username:{username}\nPassword:{new_password}")

        if is_ok:
            with open("data.txt", mode="a") as password_file:
                password_file.write(f"{website} | {username} | {new_password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, anchor=CENTER, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Label:")
website_label.grid(column=0, row=1)

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=45)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "samuelkalule@email.com")

password_label = Label(text="password")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

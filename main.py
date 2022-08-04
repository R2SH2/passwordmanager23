from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web_entry = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web_entry) <= 0 or len(password) <= 0:
        messagebox.showinfo(title='Oops', message='Please dont leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=web_entry,
                                       message=f'Email: {email} \nPassword: {password} \nAre These correct?')
        if is_ok is True:
            f = open('pass_saves.txt', 'a')
            f.write(f'{web_entry} | {email} | {password}\n')
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=20)

canvas = Canvas(height=200, width=200)
background_image = PhotoImage(file='logo.png')
canvas.create_image((100, 100), image=background_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', bd=0, width=12, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, bd=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
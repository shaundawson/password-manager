from tkinter import *
from tkinter import messagebox
import string
from random import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #       
def add_password():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok =  messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password}\n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
         
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas= Canvas(width=200, height=200, highlightthickness=2)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "iamsdawson@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
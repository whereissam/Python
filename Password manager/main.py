from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = Website_input.get()
    user = User_input.get()
    password = password_input.get()

    if website == '' or user == '' or password == '':
        messagebox.showinfo(title='Error', message='Opsss Lack some info')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: \nEmail: {user} " 
                                                  f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("save_info.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                clear_input()


def clear_input():
    Website_input.delete(0, END)
    # User_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# website info
Website_text = Label(text='Website:')
Website_text.grid(row=1, column=0)
Website_input = Entry(width=38)
Website_input.focus()
Website_input.grid(row=1, column=1, columnspan=2)

# Email info
User_text = Label(text='Email/Username:')
User_text.grid(row=2, column=0)
User_input = Entry(width=38)
User_input.insert(0, "sam@gmail.com")
User_input.grid(row=2, column=1, columnspan=2)

# Password
password_text = Label(text='Password:')
password_text.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
password_generate_button = Button(text='Generate Password')
password_generate_button.grid(row=3, column=2)

# add
add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
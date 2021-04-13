from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# pyperclip is for useful function copy and paste and very easy
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pasword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.
    # nr_symbols = random.
    # nr_numbers = random.randint(2, 4)

    # list = [(something_want_append) for char in list]
    password_letter = [choice(letters) for char in range(randint(8, 10))]
    password_symbol = [choice(symbols) for char in range(randint(2, 4))]
    password_number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    # password_list = ''
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)

    # version 1
    password = ''.join(password_list)

    #version 2
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

    # input just can use insert to put text into input
    password_input.insert(0, password)
    # after generate password copy it
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = Website_input.get()
    user = User_input.get()
    password = password_input.get()
    # to define json type first and to down below read it
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    if website == '' or user == '' or password == '':
        messagebox.showinfo(title='Error', message='Opsss Lack some info')
    else:
        # error handle, if not read it and create it
        try:
            with open("save_info.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except:
            with open("save_info.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            #if above do not have any issue and update and write new info
        else:
            #updating old data with new data
            data.update(new_data)

            with open("save_info.json", "w") as data_file:
                # saving update data
                json.dump(new_data, data_file, indent=4)
                # data_file.write(f"{website} | {user} | {password}\n")
        finally:
            clear_input()


def clear_input():
    Website_input.delete(0, END)
    # User_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def search_info():
    website = Website_input.get()
    # need add try bcu if folder do not have file and it will have erro
    try:
        with open("save_info.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No {website} detail found")



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
Website_input = Entry(width=25)
Website_input.focus()
Website_input.grid(row=1, columnspan=2, sticky=E)

# search
search_button = Button(text='Search', command=search_info)
search_button.grid(row=1, column=2)

# Email info
User_text = Label(text='Email/Username:')
User_text.grid(row=2, column=0)
User_input = Entry(width=25)
User_input.insert(0, "sam@gmail.com")
User_input.grid(row=2, columnspan=2, sticky=E)

# Password
password_text = Label(text='Password:')
password_text.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
password_generate_button = Button(text='Generate Password', command=generate_pasword)
password_generate_button.grid(row=3, column=2)

# add
add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
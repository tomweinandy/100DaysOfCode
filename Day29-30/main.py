"""
Day 29: Password Manager
"""
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a strong password of 8-10 letters, 2-4 symbols, and 2-4 numbers
    """
    # Lists of characters
    # Alternatively, this could have been created using ascii.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Select number of characters within defined range
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Randomly select characters
    list_letters = [random.choice(letters) for letter in range(nr_letters)]
    list_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    list_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    # Combine three lists into string
    password_list = list_letters + list_symbols + list_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Add to entry box in popup
    password_entry.insert(0, password)

    # Save to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """
    Saves password as a json file
    """
    # Compile entry
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        website: {
            'username': username,
            'password': password
        }
    }

    # Ask user with pop-up if info correct
    is_ok = messagebox.askokcancel(message=f'Website: {website}'
                                           f'\nEmail/Username: {username}'
                                           f'\nPassword: {password} \nIs it okay to save?')

    # Check for non-empty entries
    if len(website) > 0 and len(username) > 0 and len(password) > 0:

        if is_ok:
            # If file exists
            try:
                # Open txt file of passwords
                with open('data.json', 'r') as file:
                    # Read old data
                    data = json.load(file)
                    # Update new dats
                    data.update(new_entry)

            # If file does not exist
            except FileNotFoundError:
                data = new_entry

            with open('data.json', 'w') as file:
                # Save update to file
                json.dump(data, file, indent=4)

            # Delete text in entry (from index 0 to end)
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

    else:
        messagebox.showerror(title='Invalid Entry', message='You may not have an empty entry.')


# ------------------------- WEBSITE SEARCH ---------------------------- #
def find_password():
    """
    Searches for the username and password from the json file
    """
    try:
        # Show website details in a popup
        website = website_entry.get()
        with open('data.json', 'r') as file:
            data = json.load(file)

        messagebox.showinfo(message=f'{website}'
                                    f'\nUsername: {data[website]["username"]}'
                                    f'\n Password: {data[website]["password"]}')

    # Show error in popup
    except FileNotFoundError:
        messagebox.showerror(message='No Data File Found')

    # Show error in popup
    except KeyError:
        messagebox.showerror(title='ERROR', message='No details for the website exists')


# ---------------------------- UI SETUP ------------------------------- #
# Initialize window
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Add logo
canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Add website row
website_text = 'Website:'
website_label = tkinter.Label(text=website_text)
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = tkinter.Button(text='Search', command=find_password, width=13)
website_button.grid(row=1, column=2)

# Add username row
username_text = 'Email/Username:'
username_label = tkinter.Label(text=username_text)
username_label.grid(row=2, column=0)

username_entry = tkinter.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'example@gmail.com')

# Add password row
password_text = 'Password:'
password_label = tkinter.Label(text=password_text)
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = tkinter.Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

# Add addition row
password_button = tkinter.Button(text='Add', command=add_password, width=36)
password_button.grid(row=4, column=1, columnspan=2)


# Add main while loop to keep window open
window.mainloop()

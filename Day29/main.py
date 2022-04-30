"""
Day 29: Password Manager
"""
import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # Compile entry
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = f'{website} | {username} | {password}\n'

    # Open txt file of passwords
    with open('data.txt', 'a') as file:
        file.write(new_entry)

    # Delete text in entry
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)



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

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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

# Add add row
password_button = tkinter.Button(text='Add', command=add_password, width=36)
password_button.grid(row=4, column=1, columnspan=2)





# Add main while loop to keep window open
window.mainloop()

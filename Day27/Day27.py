"""
Day 27
"""
import tkinter


def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label['text'] = new_text


window = tkinter.Tk()
window.title('My First GUI Interface')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=2, row=0)

# New button
new_button = tkinter.Button(text='Click me too', command=button_clicked)
new_button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# Keeps window open
window.mainloop()



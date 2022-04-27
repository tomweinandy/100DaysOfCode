"""
Day 27: GUI Miles to Kilometers Converter
"""
import tkinter

FONT = ('Arial', 24)


def button_clicked():
    """
    Converts miles to kilometers and updates label
    """
    miles = int(entry.get())
    km = miles*1.60934
    km = round(km, 3)
    label3['text'] = km
    print(f'{miles} mile(s) is equal to {km} kilometers')


# Initializes tkinter window (with 100x100 padding)
window = tkinter.Tk()
window.title('Mile to Kilometer Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Adds label1
label1 = tkinter.Label(text='Mile(s)', font=FONT)
label1.grid(row=0, column=2)

# Adds label2
label2 = tkinter.Label(text='is equal to', font=FONT)
label2.grid(row=1, column=0)

# Adds label3
label3 = tkinter.Label(text='0', font=FONT)
label3.grid(row=1, column=1)

# Adds label4
label4 = tkinter.Label(text='Km', font=FONT)
label4.grid(row=1, column=2)

# Adds button
button = tkinter.Button(text='Calculate', command=button_clicked, font=FONT)
button.grid(row=2, column=1)

# Adds entry
entry = tkinter.Entry(width=10, font=FONT)
entry.insert(tkinter.END, string='0')
print(entry.get())
entry.grid(row=0, column=1)

# Keeps window open
window.mainloop()

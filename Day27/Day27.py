"""
Day 27: GUI Miles to Kilometers Converter
"""
import tkinter

LABEL_FONT = ('Arial', 24)


def button_clicked():
    miles = int(entry.get())
    km = miles*1.60934
    km = round(km, 3)
    label3['text'] = km
    print(f'{miles} mile(s) is equal to {km} kilometers')


window = tkinter.Tk()
window.title('Mile to Kilometer Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label1
label1 = tkinter.Label(text='Mile(s)', font=LABEL_FONT)
label1.grid(row=0, column=2)

# Label2
label2 = tkinter.Label(text='is equal to', font=LABEL_FONT)
label2.grid(row=1, column=0)

# Label3
label3 = tkinter.Label(text='0', font=LABEL_FONT)
label3.grid(row=1, column=1)

# Label4
label4 = tkinter.Label(text='Km', font=LABEL_FONT)
label4.grid(row=1, column=2)

# Button
button = tkinter.Button(text='Calculate', command=button_clicked, font=LABEL_FONT)
button.grid(row=2, column=1)

# Entry
entry = tkinter.Entry(width=10, font=LABEL_FONT)
entry.insert(tkinter.END, string='0')
print(entry.get())
entry.grid(row=0, column=1)


# Keeps window open
window.mainloop()



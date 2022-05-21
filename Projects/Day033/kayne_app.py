"""
An app that shows a new Kayne West quote each time it is clicked. Not the main project of the day though.
"""
from tkinter import *
import requests


def get_quote():
    kanye_url = 'https://api.kanye.rest/'
    response = requests.get(url=kanye_url)

    if response.status_code != 200:
        response.raise_for_status()
        return response.status_code

    else:
        quote = response.json()['quote']
        return quote


def get_another_quote():
    global quote_text
    another_quote = get_quote()
    canvas.itemconfig(quote_text, tex=another_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
kayne_quote = get_quote()
quote_text = canvas.create_text(150, 207, text=kayne_quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_another_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
# Anoushka Saha
# Taylor Swift Quotes
# Day 34 Project
# July 5th, 2024

from tkinter import *
import requests

def get_quote():
    response = requests.get("https://taylorswiftapi.onrender.com/get")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

# Window configurations
window = Tk()
window.minsize(width=600, height=550)
window.title("Taylor Says...")
window.config(padx=20, pady=20, bg="#FFF7AD")

canvas = Canvas(window, width=550, height=500)
canvas.config(bg="#FFF7AD", highlightthickness=0)
canvas.pack()

quote_bg = PhotoImage(file="background.png")
card_image = canvas.create_image(275, 250, image=quote_bg)

button_img = PhotoImage(file="button.png")
next_button = Button(window, image=button_img, highlightthickness=0, command=get_quote)
next_button.place(x=60, y=370)

quote_text = canvas.create_text(180, 207, text="Taylor Quote Goes HERE", width=250, font=("Cooper Black", 30), fill="black")

window.mainloop()

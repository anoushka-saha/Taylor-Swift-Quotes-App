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
    song = data["song"]
    album = data["album"]
    canvas.itemconfig(quote_text, text=quote)
    canvas.itemconfig(song_text, text=f"Song: {song}")
    canvas.itemconfig(album_text, text=f"Album: {album}")

#Window configurations
window = Tk()
window.minsize(width=600, height=550)
window.title("Taylor Says...")
window.config(padx=20, pady=20, bg="#FFF7AD")

canvas = Canvas(window, width=550, height=500)
canvas.config(bg="#FFF7AD", highlightthickness=0)
canvas.pack()

#Setting background image
quote_bg = PhotoImage(file="background.png")
card_image = canvas.create_image(275, 250, image=quote_bg)

#Setting button image
button_img = PhotoImage(file="button.png")
next_button = Button(window, image=button_img, highlightthickness=0, command=get_quote)
next_button.place(x=60, y=370)

#Title text
title_text = canvas.create_text(180, 65, text = "Taylor Says...", width = 500, font = ("Edwardian Script ITC", 40, "bold"), fill = "deeppink4")

#Displaying quote
quote_text = canvas.create_text(255, 220, text="Taylor Quote Goes HERE", width=425, font=("Lucida Sans Typewriter", 20), fill="deeppink4")

#Song and album text
song_text = canvas.create_text(275, 470, text="Song: ", width=500, font=("Lucida Sans Unicode", 12, "italic"), fill="palevioletred3")
album_text = canvas.create_text(275, 490, text="Album: ", width=500, font=("Lucida Sans Unicode", 12, "italic"), fill="palevioletred3")

get_quote()

window.mainloop()

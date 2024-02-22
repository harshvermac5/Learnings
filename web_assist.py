import webbrowser
import tkinter as tk
from tkinter import Entry, Label, Button

window = tk.Tk()
window.geometry("640x320")
window.title("Web Assistant")

def search_youtube():
    query = entrybox.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query = entrybox.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_twitter():
    query = entrybox.get()
    url = f"https://twitter.com/search?q={query}"
    webbrowser.open(url)

entrylabel = Label(text="Enter your search term")
entrylabel.place(relx=0.5, rely=0.2, anchor="center")

entrybox = Entry(justify="center", width=60)
entrybox.place(relx=0.5, rely= 0.3, anchor="center")

youtube_btn = Button(text="Youtube", command=search_youtube)
youtube_btn.place(relx=0.2, rely=0.5, anchor="center")
google_btn = Button(text="Google", command=search_google)
google_btn.place(relx=0.5, rely=0.5, anchor="center")
twitter_btn = Button(text="Twitter", command=search_twitter)
twitter_btn.place(relx=0.8, rely=0.5, anchor="center")

window.mainloop()
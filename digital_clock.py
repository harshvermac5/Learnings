import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock")
window.geometry("640x320")

# function to display time
def time():
    string = strftime("%H:%M:%S\n%D")
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(window, font=("Fira code", 50), background="yellow", foreground= "black")
label.place(relx=0.5, rely=0.5, anchor="center")

time()

window.mainloop()
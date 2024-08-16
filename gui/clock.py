from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, update)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

date_label = Label(window, font=("Arial", 50), fg="#000000")
date_label.pack()

update()

window.mainloop()
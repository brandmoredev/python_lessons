from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(background=colorHex)


window = Tk()

submitButton = Button(window, text="click me", command=click)
submitButton.pack()

window.mainloop()
from tkinter import *

def submit():
    print(text.get("1.0", END))

window = Tk()
text = Text(window)
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is an infor message", message="You have clicked me!")
    # messagebox.showwarning(title="Warning", message="You have a virus")
    # messagebox.showerror(title="Error", message="Something went wrong")
    if messagebox.askokcancel(title="Ask ok or cancel", message="Do you want to proceed"):
        print("Thanks of agreeing")
    else:
        print("You have cancelled it")

window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
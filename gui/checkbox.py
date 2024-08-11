from tkinter import *

def display():
    if (x.get() == 1):
        print("You agreed")
    else:
        print("You don't agree")


window = Tk()
window.geometry("420x420")

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)

check_button.pack()

window.mainloop()
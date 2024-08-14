from tkinter import *

def doSomething(event):
    print("You pressed: "+ event.keysym)

window = Tk()
window.bind("<Key>", doSomething)

window.mainloop()
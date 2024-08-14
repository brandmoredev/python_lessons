from tkinter import *

def doSomething(event):
    print("Mouse coordinates: (" + str(event.x) + ", " + str(event.y) + ")")

window = Tk()
window.bind("<Button-1>", doSomething) #leftclick
window.bind("<Button-2>", doSomething) #scroll wheel
window.bind("<Button-3>", doSomething) #rightclick
window.bind("<Button-3>", doSomething)
window.bind("<Leave>", doSomething)
window.bind("<Motion>", doSomething)

window.mainloop()
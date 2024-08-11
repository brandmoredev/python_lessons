from tkinter import *

window = Tk()
window.geometry("420x420")

image = PhotoImage(file='gui/image.png')

count = 0

def click():
    global count
    count += 1
    print(count)

button = Button(window,
                text="Click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                image=image,
                compound='bottom'
                )


button.pack()

window.mainloop()
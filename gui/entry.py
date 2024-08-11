from tkinter import *

def submit():
    username = entry.get() #get the text on entry box
    entry.config(state=DISABLED) #disable button
    print("Hello",username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
window.geometry("420x420")

entry = Entry(window,
              font=("Arial", 50),
              fg="green",
              bg="black",
              show="*" #for not displaying the text
            )

#default text
entry.insert(0, "Hello World")


entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
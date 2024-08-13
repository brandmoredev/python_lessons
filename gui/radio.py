from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    print("You ordered", food[x.get()])

window = Tk()

x = IntVar()

for i in range(len(food)):
    radioButton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              padx=25,
                              pady=25,
                              command=order
                              )
    
    radioButton.pack()

window.mainloop()
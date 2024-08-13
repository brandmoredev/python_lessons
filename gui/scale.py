from tkinter import *

def submit():
    print("The temperature is:", scale.get(), "degrees celcius")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              tickinterval=10)
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
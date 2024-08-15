from tkinter import *
import time
from ball import *

WIDTH = 500
HEIGHT = 300

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

voleyball = Ball(canvas, 0, 0, 75, 3, 3, "white")
basketball = Ball(canvas, 0, 0, 100, 2, 2, "orange")
football = Ball(canvas, 0, 0, 90, 1, 1, "black")

while True:
    voleyball.move()
    basketball.move()
    football.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
from tkinter import *


window = Tk()

canvas = Canvas(window, height=500, width=500)
canvas.create_line(0,0,500,500, fill="blue", width=5)
canvas.create_line(500,0,0,500, fill="red", width=5)
canvas.create_arc(0,0,500,500,fill="green",start=45)
canvas.pack()

window.mainloop()
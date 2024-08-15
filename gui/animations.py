from tkinter import *
import time

WIDTH = 500
HEIGHT = 300
x_velocity = 3
y_velocity = 3

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='gui/racecar_small.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

photo_image_width = photo_image.width()
photo_image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    if coordinates[0] >= (WIDTH - photo_image_width) or coordinates[0] < 0:
        x_velocity = -x_velocity

    if coordinates[1] >= (HEIGHT - photo_image_height) or coordinates[1] < 0:
        y_velocity = -y_velocity

 
    canvas.move(my_image,x_velocity,y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
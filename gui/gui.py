from tkinter import *

window = Tk() #instantiate a window object
window.geometry("420x420")
window.title("BRM first GUI program")

icon = PhotoImage(file='gui/logo.png')
image = PhotoImage(file='gui/image.png')
window.iconphoto(True, icon)



# Create label
label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              foreground='green',
              background='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=image,
              compound='bottom'
            )

label.pack()

window.mainloop() #place window on computer screen
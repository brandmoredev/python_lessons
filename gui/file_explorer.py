from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir='C\\Users\\Brando\\Desktop',
                                          title="Open a file",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())

window = Tk()
button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()
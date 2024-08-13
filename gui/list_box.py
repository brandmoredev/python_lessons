from tkinter import *

def submit():
    food = []
    
    for i in listbox.curselection():
        food.append(listbox.get(i))

    print("You have ordered ")
    for i in food: print(i)

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  font=("Arial",40),
                  selectmode=MULTIPLE)
listbox.pack()

entry = Entry(window)
entry.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"burger")
listbox.insert(3,"pasta")
listbox.insert(4,"hotdog")
listbox.insert(5,"bread")

listbox.config(height=listbox.size())

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()


window.mainloop()
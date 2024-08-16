from tkinter import Button

class CalculatorButton:
    def __init__(self, frame, text, height, width, row, column, command, columnspan=1) -> None:
        self.frame = frame
        self.text = text
        self.height = height
        self.row = row
        self.column = column
        self.button = Button(frame, text=text, height=height, width=width, font=35, command=command)
        self.button.grid(row=row, column=column, columnspan=columnspan)
    

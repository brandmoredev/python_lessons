from tkinter import *
from button import CalculatorButton

class SimpleCalculator:
    def __init__(self, window,):
        self.window = window
        self.window.title("Simple Calculator")
        self.window.geometry("500x500")

        self.equation_text = ""
        self.equation_label = StringVar()

        #display label
        self.display_label = Label(window, textvariable=self.equation_label, font=("consolas", 20), bg="white", width=29, height=2)
        self.display_label.pack()

        #frame
        self.frame = Frame(window)
        self.frame.pack()

        #display buttons
        self.createButtons()

        #bind keyboard events
        self.window.bind("<KeyPress>", self.handle_key_press)

    def button_press(self, text):

        #do not pressing operations at first instance
        if len(self.equation_text) == 0 and text in ["+", "-", "*", "/"]:
            return

        #do not allow consecutive operators
        elif len(self.equation_text) > 0 and self.equation_text[-1] in ["+", "-", "*", "/"] and text in ["+", "-", "*", "/"]:
            # Replace the last operator with the new one
            self.equation_text = self.equation_text[:-1] + text
        else:
            self.equation_text = self.equation_text + str(text)
        
        self.equation_label.set(self.equation_text)

    def equals(self):
        #removes operator if it is the last expression
        if len(self.equation_text) > 0 and self.equation_text[-1] in ["+", "-", "*", "/"]:
            self.equation_text = self.equation_text[:-1]

        try:
            total = str(eval(self.equation_text))

            self.equation_label.set(total)

            self.equation_text = total
        except ZeroDivisionError:
            self.equation_label.set("Arithmetic Error")
            self.equation_text = ""
        

    def clear(self):
        self.equation_text = ""
        self.equation_label.set(self.equation_text)

    def handle_key_press(self, event):
        key = event.keysym

        if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.button_press(key)
        elif key in ["plus", "minus","asterisk", "slash"]:
            op_map = {"plus": "+", "minus": "-", "asterisk": "*", "slash": "/"}
            self.button_press(op_map[key])
        elif key == "Return":
            self.equals()

    def createButtons(self):
        CalculatorButton(self.frame, 1, 4, 9, 0, 0, lambda: self.button_press(1))
        CalculatorButton(self.frame, 2, 4, 9, 0, 1, lambda: self.button_press(2))
        CalculatorButton(self.frame, 3, 4, 9, 0, 2, lambda: self.button_press(3))
        CalculatorButton(self.frame, 4, 4, 9, 1, 0, lambda: self.button_press(4))
        CalculatorButton(self.frame, 5, 4, 9, 1, 1, lambda: self.button_press(5))
        CalculatorButton(self.frame, 6, 4, 9, 1, 2, lambda: self.button_press(6))
        CalculatorButton(self.frame, 7, 4, 9, 2, 0, lambda: self.button_press(7))
        CalculatorButton(self.frame, 8, 4, 9, 2, 1, lambda: self.button_press(8))
        CalculatorButton(self.frame, 9, 4, 9, 2, 2, lambda: self.button_press(9))
        CalculatorButton(self.frame, '+', 4, 9, 0, 3, lambda: self.button_press('+'))
        CalculatorButton(self.frame, '-', 4, 9, 1, 3, lambda: self.button_press('-'))
        CalculatorButton(self.frame, '*', 4, 9, 2, 3, lambda: self.button_press('*'))
        CalculatorButton(self.frame, '/', 4, 9, 3, 3, lambda: self.button_press('/'))
        CalculatorButton(self.frame, 0, 4, 9, 3, 1, lambda: self.button_press(0))
        CalculatorButton(self.frame, '=', 4, 9, 3, 2, self.equals)
        CalculatorButton(self.frame, 'C', 4, 9, 3, 0, self.clear)



window = Tk()
app = SimpleCalculator(window)
window.mainloop()
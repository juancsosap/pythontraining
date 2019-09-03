import tkinter as tk
from controller import CalculatorController as Controller

class CalculatorView(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")

        self.__add_elements()
        
        self.controller = Controller(self)

        self.mainloop()

    def __add_elements(self):
        self.label_num1 = tk.Label(self, text='Number 1')
        self.label_num1.grid(row=0, column=0, sticky='E')
        self.entry_num1 = tk.Entry(self)
        self.entry_num1.grid(row=0, column=1)
        
        self.label_num2 = tk.Label(self, text='Number2')
        self.label_num2.grid(row=1, column=0, sticky='E')
        self.entry_num2 = tk.Entry(self)
        self.entry_num2.grid(row=1, column=1)
        
        self.button_calc = tk.Button(self, text='Calculate')
        self.button_calc.grid(row=2, columnspan=2)

        self.label_result = tk.Label(self, text='Result')
        self.label_result.grid(row=3, columnspan=2)

if __name__ == "__main__":
    CalculatorView()
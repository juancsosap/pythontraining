import tkinter as tk
import tkinter.messagebox as tkm

class CalculatorController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.button_calc.bind('<Button-1>', self.calculate)

        self.num1 = tk.IntVar()
        self.window.entry_num1.config(textvariable=self.num1)
        self.num2 = tk.IntVar()
        self.window.entry_num2.config(textvariable=self.num2)
        
    def calculate(self, event):
        try:
            result = self.num1.get() + self.num2.get()

            result_str = 'Result: {}'.format(result)
            self.window.label_result.config(text=result_str)
            tkm.showinfo("Result", str(result_str))
        except:
            tkm.showerror("Error", "Invalid Input")

    def close_window(self, event):
        self.window.destroy()
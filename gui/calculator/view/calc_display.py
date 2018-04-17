from tkinter import Entry
from calculator.controller import DisplayCalcController


class DisplayCalc(Entry):
    def __init__(self, window, row):
        super(DisplayCalc, self).__init__(window)

        self.grid(row=row, column=1, padx=10, pady=10)
        self.config(bg="black", fg="#03f943", justify="right")

    def addcontroller(self, window):
        self.controller = DisplayCalcController(window)

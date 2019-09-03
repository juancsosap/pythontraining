from tkinter import Entry
from calculator.controller import DisplayCalcController


class DisplayCalc(Entry):
    def __init__(self, window, row):
        super(DisplayCalc, self).__init__(window)

        self.grid(row=row, column=1, padx=10, pady=10)
        self.config(bg="black", fg="white", justify="right")
        self.config(width=60)

    def addcontroller(self, window):
        self.controller = DisplayCalcController(window)

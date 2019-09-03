from tkinter import StringVar


class DisplayCalcController:
    def __init__(self, window):
        self.display = StringVar()
        window.display.config(textvariable=self.display)

    def add(self, value):
        self.display.set(self.display.get() + value)

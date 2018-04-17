from tkinter import Tk, Frame, Entry
from calculator.view import DisplayCalc, ButtonsCalc


class WindowCalc(Tk):
    def __init__(self):
        super(WindowCalc, self).__init__()

        self.display = DisplayCalc(self, 1)
        self.display.addcontroller(self)
        self.buttons = ButtonsCalc(self, 2)
        self.buttons.addcontroller(self)

        self.mainloop()

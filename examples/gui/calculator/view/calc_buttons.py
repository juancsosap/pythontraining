from tkinter import Frame, Button
from calculator.controller import ButtonsCalcController


class ButtonsCalc(Frame):
    def __init__(self, window, row):
        super(ButtonsCalc, self).__init__(window)

        self.buttons = [[], [], [], []]
        self.buttons_texts = [['7', '8', '9', '/'],
                              ['4', '5', '6', 'x'],
                              ['1', '2', '3', '-'],
                              ['=', '0', '.', '+']]

        for i in range(4):
            for j in range(4):
                boton = Button(self, text=self.buttons_texts[i][j])
                boton.config(width=10, height=5)
                boton.config(font='Arial')
                self.buttons[i].append(boton)
                self.buttons[i][j].grid(row=(i + 2), column=(j + 1))

        self.grid(row=row, column=1, padx=10, pady=10)

    def addcontroller(self, window):
        self.controller = ButtonsCalcController(window)

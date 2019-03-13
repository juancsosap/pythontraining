from tkinter import StringVar


class ButtonsCalcController:
    def __init__(self, window):
        for i in range(4):
            for j in range(4):
                texts = window.buttons.buttons_texts
                if texts[i][j].isnumeric():
                    window.buttons.buttons[i][j].config(
                        command=lambda: window.display.controller.add(texts[i][j]))

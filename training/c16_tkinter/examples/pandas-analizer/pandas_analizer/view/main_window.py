import tkinter as tk
from pandas_analizer import MainController

import os


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__add_labels()
        self.__add_entries()
        self.__add_buttons()

        self.controller = MainController(self)

        self.title('Pandas Analizer')
        self.resizable(False, False)

        #dir = os.path.abspath(os.path.dirname(__file__))
        #image_path = os.path.join(dir, 'images/plot.ico')
        #self.iconbitmap(image_path)

        self.mainloop()

    def __add_labels(self):
        self.label_path = tk.Label(self, text='Ruta Data Origen:')
        self.label_path.grid(row=0, sticky='W', pady=5, padx=10)
        self.label_field = tk.Label(self, text='Campo a Analizar:')
        self.label_field.grid(row=2, sticky='W', pady=5, padx=10)

    def __add_entries(self):
        self.entry_path = tk.Entry(self, width=50)
        self.entry_path.grid(row=1, padx=10)
        self.entry_field = tk.Entry(self, width=50)
        self.entry_field.grid(row=3, padx=10)

    def __add_buttons(self):
        panel_buttons = tk.Frame(self)
        panel_buttons.grid(row=4, sticky='E', pady=10, padx=10)

        self.button_mean = tk.Button(panel_buttons, text='Media')
        self.button_mean.pack(side='right', padx=5)
        self.button_plot = tk.Button(panel_buttons, text='Grafico')
        self.button_plot.pack(side='right', padx=5)

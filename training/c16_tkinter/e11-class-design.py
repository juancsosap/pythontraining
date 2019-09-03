import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__add_label_elements()
        self.__add_entry_elements()
        self.__add_checkbox_elements()
        self.__add_button_elements()

        self.controller = MainController(self)

        self.mainloop()

    def __add_label_elements(self):
        self.label_nick = tk.Label(self, text='Nick')
        self.label_nick.grid(row=0, column=0, sticky='E')
        self.label_password = tk.Label(self, text='Password')
        self.label_password.grid(row=1, column=0, sticky='E')

    def __add_entry_elements(self):
        self.entry_nick = tk.Entry(self)
        self.entry_nick.grid(row=0, column=1)
        self.entry_password = tk.Entry(self, show='*')
        self.entry_password.grid(row=1, column=1)

    def __add_checkbox_elements(self):
        self.check_logged = tk.Checkbutton(self, text='Keep me logged in')
        self.check_logged.grid(row=3, columnspan=2)

    def __add_button_elements(self):
        self.button_close = tk.Button(self, text='Close')
        self.button_close.grid(row=4, column=0, sticky='W')
        self.button_clean = tk.Button(self, text='Colored')
        self.button_clean.grid(row=4, column=1, sticky='E')


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.button_close.bind('<Button-1>', self.close_window)
        self.window.button_clean.bind('<Button-1>', self.paint_entries)

    def paint_entries(self, event):
        self.window.entry_nick.config(bg='red', fg='white')
        self.window.entry_password.config(bg='red', fg='white')

    def close_window(self, event):
        self.window.destroy()


if __name__ == '__main__':
    MainWindow()
    MainWindow()

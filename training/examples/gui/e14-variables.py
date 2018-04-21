import tkinter as tk
import tkinter.messagebox as tkm


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__add_labels()
        self.__add_entries()
        self.__add_buttons()

        self.controller = MainController(self)

        self.title('Calc')
        self.resizable(False, False)
        self.mainloop()

    def __add_labels(self):
        self.label_A = tk.Label(self, text='Num A:')
        self.label_A.grid(row=0, column=0, sticky='E', pady=5, padx=5)
        self.label_B = tk.Label(self, text='Num B:')
        self.label_B.grid(row=1, column=0, sticky='E', pady=5, padx=5)

    def __add_entries(self):
        self.entry_A = tk.Entry(self)
        self.entry_A.grid(row=0, column=1, pady=5, padx=5)
        self.entry_B = tk.Entry(self)
        self.entry_B.grid(row=1, column=1, pady=5, padx=5)

    def __add_buttons(self):
        panel_buttons = tk.Frame(self)
        panel_buttons.grid(row=2, column=1, sticky='E', pady=5, padx=5)

        self.button_add = tk.Button(panel_buttons, text='Add')
        self.button_add.pack(side='right', padx=5)
        self.button_sub = tk.Button(panel_buttons, text='Sub')
        self.button_sub.pack(side='right', padx=5)


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.quit)

        self.__init_variables()
        self.__init_button_commands()

    def __init_variables(self):
        self.num_a = tk.IntVar()
        self.window.entry_A.config(textvariable=self.num_a)
        self.num_b = tk.IntVar()
        self.window.entry_B.config(textvariable=self.num_b)

    def __init_button_commands(self):
        self.window.button_add.config(command=self.add)
        self.window.button_sub.config(command=self.sub)

    def quit(self):
        self.window.destroy()

    def add(self):
        result = self.num_a.get() + self.num_b.get()
        tkm.showinfo("Result", "The Addition result is {result}".format(result=result))

    def sub(self):
        result = self.num_a.get() - self.num_b.get()
        tkm.showinfo("Result", "The Substraction result is {result}".format(result=result))


if __name__ == '__main__':
    MainWindow()

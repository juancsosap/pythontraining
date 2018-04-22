import tkinter as tk
import tkinter.messagebox as tkm


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__add_menus()
        self.__add_toolbar()
        self.__add_statusbar()

        self.controller = MainController(self)

        self.mainloop()

    def __add_menus(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Print')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close')

        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='About')
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='Info')

    def __add_toolbar(self):
        self.toolbar = tk.Frame(self, bg='blue')
        self.toolbar.pack(side='top', fill='x')

        self.button_close = tk.Button(self.toolbar, text="Close")
        self.button_close.pack(side='left', padx=2, pady=2)
        self.button_print = tk.Button(self.toolbar, text="Print")
        self.button_print.pack(side='left', padx=2, pady=2)
        self.button_about = tk.Button(self.toolbar, text="About")
        self.button_about.pack(side='left', padx=2, pady=2)
        self.button_info = tk.Button(self.toolbar, text="Info")
        self.button_info.pack(side='left', padx=2, pady=2)

    def __add_statusbar(self):
        self.statusbar = tk.Label(self, text='Application Active',
                                  bd=1, relief='sunken', anchor='w')
        self.statusbar.pack(side='bottom', fill='x')


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.quit)

        self.window.filemenu.entryconfigure('Print', command=self.print)
        self.window.filemenu.entryconfigure('Close', command=self.quit)
        self.window.helpmenu.entryconfigure('About', command=self.about)
        self.window.helpmenu.entryconfigure('Info', command=self.info)

        self.window.button_close.config(command=self.quit)
        self.window.button_print.config(command=self.print)
        self.window.button_about.config(command=self.about)
        self.window.button_info.config(command=self.info)

    def quit(self):
        if(tkm.askokcancel("Closing", "The windows will be close\nAre you sure?")):
            self.window.destroy()

    def print(self):
        tkm.showwarning("Printing", "Thanks, for click me")

    def about(self):
        tkm.showerror("About", "This is a good program")

    def info(self):
        tkm.showinfo("Info", "The author are you")


if __name__ == '__main__':
    MainWindow()

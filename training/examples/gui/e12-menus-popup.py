import tkinter as tk
import tkinter.messagebox as tkm


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.controller = MainController(self)

        self.__add_menus()

        self.mainloop()

    def __add_menus(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Print', command=self.controller.print)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.controller.quit)

        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='About', command=self.controller.about)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='Info', command=self.controller.info)


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.quit)

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

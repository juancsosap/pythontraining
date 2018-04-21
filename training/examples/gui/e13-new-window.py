import tkinter as tk
import tkinter.messagebox as tkm


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.controller = MainController(self)

        self.__add_menus()

        self.title('Main')
        self.mainloop()

    def __add_menus(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New Window ...', command=self.controller.new)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.controller.quit)


class OtherWindow(tk.Tk):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.controller = OtherController(self)

        self.title('Other')
        self.mainloop()


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.quit)

    def quit(self):
        if(tkm.askokcancel("Closing", "The windows will be close\nAre you sure?")):
            self.window.destroy()

    def new(self):
        self.window.withdraw()
        self.newwindow = OtherWindow(self.window)


class OtherController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.quit)

    def quit(self):
        self.window.destroy()
        self.window.parent.update()
        self.window.parent.deiconify()


if __name__ == '__main__':
    MainWindow()

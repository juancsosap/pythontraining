import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__add_canvas()
        self.__add_shapes()

        self.mainloop()

    def __add_canvas(self):
        self.canvas = tk.Canvas(self, width=200, height=100)
        self.canvas.pack()

    def __add_shapes(self):
        self.blackline = self.canvas.create_line(0, 0, 200, 100)
        self.redline = self.canvas.create_line(0, 100, 200, 0, fill='red')

        self.greenbox = self.canvas.create_rectangle(50, 25, 150, 75, fill='green')

        self.canvas.delete(self.blackline)


if __name__ == '__main__':
    MainWindow()

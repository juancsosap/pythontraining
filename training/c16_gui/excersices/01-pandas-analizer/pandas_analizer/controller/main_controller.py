import tkinter as tk
import tkinter.messagebox as tkm
import pandas as pd
import matplotlib.pyplot as plt


class MainController():

    def __init__(self, window):
        self.window = window

        self.__initial_config()

    def __initial_config(self):
        self.window.protocol('WM_DELETE_WINDOW', self.window.destroy)

        self.__init_variables()
        self.__init_button_commands()

    def __init_variables(self):
        self.path = tk.StringVar()
        self.window.entry_path.config(textvariable=self.path)
        self.field = tk.StringVar()
        self.window.entry_field.config(textvariable=self.field)

    def __init_button_commands(self):
        self.window.button_mean.config(command=self.mean)
        self.window.button_plot.config(command=self.plot)

    def mean(self):
        data = pd.read_csv(self.path.get())
        mean_val = data[self.field.get()].mean()
        msg = "La media total calculada fue de \n\n{mean}".format(mean=mean_val)
        tkm.showinfo("Resultados", msg)

    def plot(self):
        data = pd.read_table(self.path.get(), sep='\t')
        data.groupby(self.field.get()).mean().plot.bar()
        plt.xticks(rotation=45)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel(self.field.get().capitalize())
        plt.ylabel('Mean Value')
        plt.title('Mean Graph per {field}'.format(field=self.field.get().capitalize()))
        plt.grid(True)
        plt.show()

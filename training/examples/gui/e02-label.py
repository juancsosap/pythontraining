import tkinter as tk


window = tk.Tk()

label1 = tk.Label(window, text='This is my first Label widgets in TKinter')
label1.config(bg='red', fg='white')
label1.pack()

label2 = tk.Label(window, text='This is my second Label widgets in TKinter')
label2.config(bg='blue', fg='gray')
label2.pack(fill='x')

label3 = tk.Label(window, text='This is my third Label widgets in TKinter')
label3.config(bg='brown', fg='yellow')
label3.pack(fill='y', side='left')

window.mainloop()

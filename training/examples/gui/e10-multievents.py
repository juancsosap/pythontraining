import tkinter as tk


def close_window_left(event):
    button_close.config(bg='red')


def close_window_center(event):
    button_close.config(bg='green')


def close_window_right(event):
    button_close.config(bg='blue')


window = tk.Tk()

label_nick = tk.Label(window, text='Nick')
label_nick.grid(row=0, column=0, sticky='E')

label_password = tk.Label(window, text='Password')
label_password.grid(row=1, column=0, sticky='E')

entry_nick = tk.Entry(window)
entry_nick.grid(row=0, column=1)

entry_password = tk.Entry(window, show='*')
entry_password.grid(row=1, column=1)

check_logged = tk.Checkbutton(window, text='Keep me logged in')
check_logged.grid(row=3, columnspan=2)

button_close = tk.Button(window, text='Close')
button_close.grid(row=4, column=0, sticky='W')
button_close.bind('<Button-1>', close_window_left)
button_close.bind('<Button-2>', close_window_center)
button_close.bind('<Button-3>', close_window_right)

window.mainloop()

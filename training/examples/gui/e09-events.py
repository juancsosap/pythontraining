import tkinter as tk


def clean_entries(event):
    entry_nick.text = ''
    entry_password.text = ''


def close_window(event):
    window.destroy()


window = tk.Tk()

label_nick = tk.Label(window, text='Nick')
label_nick.grid(row=0, column=0, sticky='E')

label_password = tk.Label(window, text='Password')
label_password.grid(row=1, column=0, sticky='E')

entry_nick = tk.Entry(window)
entry_nick.grid(row=0, column=1)

entry_password = tk.Entry(window)
entry_password.grid(row=1, column=1)

check_logged = tk.Checkbutton(window, text='Keep me logged in')
check_logged.grid(row=3, columnspan=2)

button_close = tk.Button(window, text='Close')
button_close.grid(row=4, column=0, sticky='W')
button_close.bind('<Button-1>', close_window)

button_clean = tk.Button(window, text='Clean')
button_clean.grid(row=4, column=1, sticky='E')
button_clean.bind('<Button-1>', clean_entries)

window.mainloop()

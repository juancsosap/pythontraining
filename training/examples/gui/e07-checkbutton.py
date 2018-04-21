import tkinter as tk


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

window.mainloop()

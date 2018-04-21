import tkinter as tk
# pip install tkinter


window = tk.Tk()

top_panel = tk.Frame(window)
top_panel.config(width=200, height=200, bg='red')
top_panel.pack(side='top')  # Default

bottom_panel = tk.Frame(window)
bottom_panel.config(width=200, height=200, bg='blue')
bottom_panel.pack(side='bottom')

button1 = tk.Button(top_panel, text='Button 1', fg='red')
button2 = tk.Button(top_panel, text='Button 2', fg='blue')
button3 = tk.Button(top_panel, text='Button 3', fg='green')
button4 = tk.Button(bottom_panel, text='Button 4', fg='orange')
button5 = tk.Button(bottom_panel, text='Button 5', fg='brown')
button6 = tk.Button(bottom_panel, text='Button 6', fg='grey')

button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack(side='right')
button5.pack(side='right')
button6.pack(side='right')

window.mainloop()

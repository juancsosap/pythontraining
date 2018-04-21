import tkinter as tk


window = tk.Tk()

top_panel1 = tk.Frame(window)
top_panel1.config(width=200, height=100, bg='red')
top_panel1.pack(side='top', padx=10, fill='y', expand=True)  # Default Side

top_panel2 = tk.Frame(window)
top_panel2.config(width=200, height=100, bg='green')
top_panel2.pack(side='top', padx=10, fill='y')  # Default Side

bottom_panel1 = tk.Frame(window)
bottom_panel1.config(width=200, height=100, bg='blue')
bottom_panel1.pack(side='bottom', pady=10, fill='x')

bottom_panel2 = tk.Frame(window)
bottom_panel2.config(width=200, height=100, bg='purple')
bottom_panel2.pack(side='bottom', padx=10, pady=10, fill='both', expand=True)

window.mainloop()

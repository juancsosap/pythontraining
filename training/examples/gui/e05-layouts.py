import tkinter as tk


window = tk.Tk()

panel1 = tk.Frame(window)
panel1.config(width=200, height=100, bg='red')
panel1.pack(side='top', padx=10, pady=10, fill='both', expand=True)

panel2 = tk.Frame(window)
panel2.config(width=200, height=100, bg='blue')
panel2.pack(side='top', padx=10, pady=10, fill='both', expand=True)

panel3 = tk.Frame(window)
panel3.config(width=200, height=100, bg='green')
panel3.pack(side='top', padx=10, pady=10, fill='both', expand=True)


label1_1 = tk.Label(panel1, text='Label 1 (PURPLE)', bg='purple')
label2_1 = tk.Label(panel1, text='Label 2 (BLUE)', bg='blue')
label3_1 = tk.Label(panel1, text='Label 3 (GREEN)', bg='green')
label4_1 = tk.Label(panel1, text='Label 4 (ORANGE)', bg='orange')
label5_1 = tk.Label(panel1, text='Label 5 (PINK)', bg='pink')

label1_1.grid(row=0, column=0, sticky='W', padx=10, pady=10)
label2_1.grid(row=0, column=1, sticky='E', padx=10, pady=10)
label3_1.grid(row=1, column=0, sticky='W', padx=10, pady=10)
label4_1.grid(row=1, column=1, sticky='E', padx=10, pady=10)
label5_1.grid(row=3, columnspan=2, pady=10)

label1_2 = tk.Label(panel2, text='Label 1 (RED)', bg='red')
label2_2 = tk.Label(panel2, text='Label 2 (PURPLE)', bg='purple')
label3_2 = tk.Label(panel2, text='Label 3 (GREEN)', bg='green')
label4_2 = tk.Label(panel2, text='Label 4 (ORANGE)', bg='orange')

label1_2.pack(side='left')
label2_2.pack(side='right')
label3_2.pack(side='top')
label4_2.pack(side='bottom')

label1_3 = tk.Label(panel3, text='Label 1 (RED)', bg='red')
label2_3 = tk.Label(panel3, text='Label 2 (PURPLE)', bg='purple')
label3_3 = tk.Label(panel3, text='Label 3 (BLUE)', bg='blue')
label4_3 = tk.Label(panel3, text='Label 4 (ORANGE)', bg='orange')

label1_3.place(x=10, y=10)
label2_3.place(x=20, y=25)
label3_3.place(x=150, y=10)
label4_3.place(x=10, y=50)

window.mainloop()

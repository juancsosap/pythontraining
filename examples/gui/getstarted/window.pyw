# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Label, Entry, Text, Button, Scrollbar, StringVar, IntVar


window = Tk()
window.title("My First Windows")
window.resizable(True, True)
window.config(bg="blue")

frame = Frame(window, width=650, height=350)
frame.pack(side="left", anchor="n", fill="both", expand="True")
frame.config(bg="red", bd=10, relief="groove", cursor="hand2")

label = Label(frame, text="My First Label")
label.config(bg="red", cursor="pirate")
label.place(x=100, y=50)

Label(frame, text="My Second Label", font=("Comic Sans MS", 18), bg="red").place(x=100, y=100)

entry = Entry(frame)
entry.place(x=100, y=150)

form = Frame(frame, bg="red")
form.place(x=350, y=50)

Label(form, text="Nombre", bg="red").grid(row=0, column=0, sticky="e", pady=5, padx=5)

nombre = StringVar()
ent_nombre = Entry(form, textvariable=nombre)
ent_nombre.config(fg="blue", justify="center")
ent_nombre.grid(row=0, column=1)

Label(form, text="Apellido", bg="red").grid(row=1, column=0, sticky="e", pady=5, padx=5)

apellido = StringVar()
ent_apellido = Entry(form, textvariable=apellido)
ent_apellido.config(fg="blue", justify="center")
ent_apellido.grid(row=1, column=1)

Label(form, text="Contraseña", bg="red").grid(row=2, column=0, sticky="e", pady=5, padx=5)

password = StringVar()
ent_pass = Entry(form, textvariable=password)
ent_pass.config(fg="blue", justify="center", show="*")
ent_pass.grid(row=2, column=1)

Label(form, text="Edad", bg="red").grid(row=3, column=0, sticky="e", pady=5, padx=5)

edad = IntVar()
ent_edad = Entry(form, textvariable=edad)
ent_edad.config(fg="blue", justify="center")
ent_edad.grid(row=3, column=1)

Label(form, text="Dirección", bg="red").grid(row=4, column=0, sticky="e", pady=5, padx=5)

ent_direccion = Text(form, width=15, height=5)
ent_direccion.config(fg="blue")
ent_direccion.grid(row=4, column=1)

sbv_direccion = Scrollbar(form, command=ent_direccion.yview)
sbv_direccion.grid(row=4, column=2, sticky="nsew")

ent_direccion.config(yscrollcommand=sbv_direccion.set)


def summit():
    print('Nombre:   {}'.format(nombre.get()))
    print('Apellido: {}'.format(apellido.get()))
    print('Clave:    {}'.format(password.get()))
    print('Edad:     {}'.format(edad.get()))


btn_envio = Button(form, text="Enviar", command=summit, width=16)
btn_envio.grid(row=5, column=1, sticky="w", pady=10)


window.mainloop()

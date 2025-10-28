import tkinter as tk
def r_observer(*args):
    print("Reading")
def w_observer(*args):
    print("Writing")
ventana = tk.Tk()
variable = tk.StringVar()
boton_1 = tk.Button(ventana, text="Leer", command=lambda: variable.get())
boton_2 = tk.Button(ventana, text="Escribir", command=lambda: variable.set("Hola"))
boton_3 = tk.Button(ventana, text="Dejar de observar leer", command=lambda: variable.trace_remove("read", r_obsid))
boton_1.pack()
boton_2.pack()
boton_3.pack()
r_obsid= variable.trace_add("read", r_observer)
w_obsid= variable.trace_add("write", w_observer)
ventana.mainloop()
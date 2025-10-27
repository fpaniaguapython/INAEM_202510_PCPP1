import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk # Librería GUAY

def sumar():
    try:
        sumando_1 = int(entry_sumando_1.get())
        sumando_2 = int(entry_sumando_2.get())
        resultado = sumando_1+sumando_2
        mostrar_mensaje(resultado)        
    except ValueError as ve:
        mostrar_error('Los sumandos deben ser enteros')

def mostrar_mensaje(texto: str):
    mb.showinfo('Mensaje',texto)

def mostrar_error(texto: str):
    mb.showerror('Error', texto)

if __name__=='__main__':
    # Definición de la ventana
    window = tk.Tk()
    window.title('Mi primera app')
    window.geometry('270x50')

    # Definición de un campo de entrada
    entry_sumando_1 = ttk.Entry(window)
    entry_sumando_1.place(x=10, y=10, width=50, height=30)
    #entry_sumando_1.pack()

    entry_sumando_2 = ttk.Entry(window)
    entry_sumando_2.place(x=70, y=10, width=50, height=30)
    #entry_sumando_2.pack()

    # Definición de un botón
    boton_aceptar = ttk.Button(window, text='Pulsar', command=sumar) # No implica presentación
    boton_aceptar.place(x=140, y=10, width=70, height=30)
    #boton_aceptar.pack()

    window.mainloop()
    
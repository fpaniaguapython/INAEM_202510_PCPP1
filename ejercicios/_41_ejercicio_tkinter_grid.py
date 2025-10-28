# Interfaz para la introducción de los datos de una película
# y su almacenamiento utlizando algún módulo de serialización.
# Las películas tienen Título, Director y Año de estreno.
# Utilizamos DISTRIBUCIÓN GRID.
# También podemos recuperar películas a partir del título.
# Utilizar ventanas de diálogo para notificar las acciones.
import tkinter as tk
import tkinter.messagebox as mb


from gestor_pickle_41_tkinter import GestorPickle

class Pelicula:
    def __init__(self, titulo, director, anyo):
        self.titulo=titulo
        self.director=director
        self.anyo=anyo


def guardar():
    try:
        titulo = entry_titulo.get()
        director = entry_director.get()
        anyo = int(entry_anyo.get())
        pelicula = Pelicula(titulo, director, anyo)
        GestorPickle().create(pelicula)
    except Exception as e:
        mb.showerror('Superpelis','Ha ocurrido un error')
    else:
        mb.showinfo('Superpelis','La película se ha guardado')

def leer():
    pass

window = tk.Tk()
label_titulo = tk.Label(window, text='Título')
entry_titulo = tk.Entry(window)

label_director = tk.Label(window, text='Director')
entry_director = tk.Entry(window)

label_anyo = tk.Label(window, text='Año')
entry_anyo = tk.Entry(window)

button_guardar = tk.Button(window, text='Guardar', command=guardar)
button_leer = tk.Button(window, text='Leer', command=leer)

label_titulo.grid(row=0, column=0)
entry_titulo.grid(row=0, column=1)
label_director.grid(row=1, column=0)
entry_director.grid(row=1, column=1)
label_anyo.grid(row=2, column=0)
entry_anyo.grid(row=2, column=1)
button_guardar.grid(row=3, column=0)
button_leer.grid(row=3, column=1)

def entrando(event):
    print('Entrando:', event.widget)
    print(event.__dict__)

def saliendo(event):
    print('Saliendo', event.widget)
    print(event.__dict__)

label_titulo.bind("<Enter>", entrando)
label_titulo.bind("<Leave>", saliendo)


window.mainloop()
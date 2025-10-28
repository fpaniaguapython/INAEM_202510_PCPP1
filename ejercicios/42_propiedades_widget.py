import tkinter as tk

window = tk.Tk()

def cambiar(event=None):
    print('Cambiando...', event)
    texto_boton=button_cambiar['text']
    print(texto_boton)
    button_cambiar['text']='Pulsado'
    button_cambiar['width']=int(button_cambiar['width']/2)
    button_cambiar['bg']='#00FF00'
    label_texto['text']='Cambiado'

label_texto = tk.Label(window, text='Texto')
button_cambiar = tk.Button(window, text='Pulsa', command=cambiar, width='100',bg="#611A9C")
button_cambiar.config(pady=30)
button_cambiar.bind('<Button-1>', cambiar)

label_texto.pack()
button_cambiar.pack()





window.mainloop()
def mi_decorador(funcion_decorada):
    print('Estoy ejecutando la función externa')
    def lapatata(*args, **kwargs):
        print('Estoy ejecutando la función interna')
        funcion_decorada()
    return lapatata

@mi_decorador
def saludar():
    print('Hola')

saludar()
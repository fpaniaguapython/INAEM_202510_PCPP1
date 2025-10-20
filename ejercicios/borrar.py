def decorador(funcion):
    def inner(*args, **kwargs):
        print('Decorando...')
        return funcion(*args, **kwargs)
    return inner

@decorador
def sumar(a,b):
    return a+b

resultado = sumar(2,1)
print(resultado)
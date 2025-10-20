def decorador_1(funcion):
    def inner_function(*args, **kwargs):
        print('*****')
        retorno = funcion(*args, **kwargs)
        print('*****')
        return retorno
    return inner_function

def decorador_2(funcion):
    def inner_function(*args, **kwargs):
        print('+++++')
        retorno = funcion(*args, **kwargs)
        print('+++++')
        return retorno
    return inner_function

@decorador_2
@decorador_1
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Saúl')
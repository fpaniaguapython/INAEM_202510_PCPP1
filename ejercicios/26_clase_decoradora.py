class Decorador:
    def __init__(self, funcion_decorada):
        print('En el init:', funcion_decorada)
        self.funcion_decorada = funcion_decorada

    def __call__(self, *args, **kwargs):
        print('Código del decorador...')
        return self.funcion_decorada(*args, **kwargs)

@Decorador
def funcion_a_decorar(*args, **kwargs):
    print('Función decorada:', args, kwargs)
    return 'OK'

print(funcion_a_decorar('Python'))


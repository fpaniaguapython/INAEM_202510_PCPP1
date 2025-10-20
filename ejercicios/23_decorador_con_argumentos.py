from datetime import datetime

def escribir_log(nombre_fichero, nombre_funcion, timestamp):
    with open(nombre_fichero,mode='a',encoding='utf-8') as fichero_log:
        fichero_log.write(f'{nombre_funcion}:{timestamp}')
        fichero_log.write('\n')

def registrar_log(nombre_fichero):
    def outer_function(funcion_a_decorar):
        def inner_function(*args, **kwargs):
            escribir_log(nombre_fichero, funcion_a_decorar.__name__, str(datetime.now()))
            funcion_a_decorar(*args, **kwargs)
        return inner_function
    return outer_function

@registrar_log('mi_log.txt')
def saludar(nombre):
    print(f'Hola {nombre}')

@registrar_log('tu_log.txt')
def calcular(numero_1, numero_2):
    print(numero_1+numero_2)

saludar('Felipe')
calcular(10,4)
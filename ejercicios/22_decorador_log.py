from datetime import datetime

def escribir_log(nombre_funcion, timestamp):
    with open('log.txt',mode='a',encoding='utf-8') as fichero_log:
        fichero_log.write(f'{nombre_funcion}:{timestamp}')
        fichero_log.write('\n')

def registrar_log(funcion_a_decorar):
    def inner_function(*args, **kwargs):
        escribir_log(funcion_a_decorar.__name__, str(datetime.now()))
        funcion_a_decorar(*args, **kwargs)
    return inner_function

@registrar_log
def saludar(nombre):
    print(f'Hola {nombre}')

@registrar_log
def calcular(numero_1, numero_2):
    print(numero_1+numero_2)

#saludar('Felipe')
calcular(10,4)
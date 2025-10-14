# 3 funciones que muestren un mensaje por pantalla
# Crear una lista
# Agregar a la lista los nombres de las funciones

def copiar():
    print('Copiando')
    return

def pegar():
    print('Pegando')
    return

def cortar():
    print('Cortando')
    return

def ejecutar(lista_funciones):
    for funcion in lista_funciones:
        funcion()

lista_funciones = list()
lista_funciones.append(pegar)
lista_funciones.append(cortar)
lista_funciones.append(copiar)

ejecutar(lista_funciones)
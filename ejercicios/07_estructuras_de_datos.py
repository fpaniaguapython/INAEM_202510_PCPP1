def f():
    pass

lista = [1, 'Café', 8.3, True, f]
lista.append('otro elemento')
lista.insert(1, 'ColaCao')
lista[2]=8.4
elemento = lista.pop() # Obtener y eliminar
lista = [3, 8, -1, 15, 2]
lista.sort()
nueva_lista = list()

tupla = (1,2,3,4)
tupla_2 = ()
tupla_3 = (1,) # Si solo hay un elemento, se considera expresión

conjunto = {}
conjunto = {1, 'Automóvil', 'Zamora', 'Zamora', 'Júpiter'}
print(conjunto)
conjunto = set()

diccionario = {'Huesca':150_000, 'Teruel':80_000, 'Zaragoza':987_763}
print(diccionario.get('Huesca'))
print(diccionario.get('Castellón', '¿De qué vas?'))


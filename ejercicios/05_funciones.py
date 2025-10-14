def calcular_importe(x:int, y:int, z:int=0) ->int:
    print(x, y, z)
    return x+y+z

calcular_importe(10,5)
calcular_importe(10,5,8)
calcular_importe(y=8, x=8)

mi_funcion = calcular_importe
mi_funcion(12,8)

def calcular(*args):
    print(args)
    print(type(args))

calcular(10,20,30,'Hola',True)

def validar(**kwargs):
    print(kwargs)
    print(type(kwargs))

validar(x=10, y=12, z=50)
